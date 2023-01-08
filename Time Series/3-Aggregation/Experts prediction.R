library(randomForest)
library(forecast)
library(gbm)
library(opera)
library(dplyr)

###Load Data
df = read.csv("https://raw.githubusercontent.com/Tdjaaleb/MALIA/main/Time%20Series/Preprocessing/Data/clean_National.csv", sep=';')
X_train = subset(na.omit(df[1:52561,]), select = -c(Conso, ConsoT.1, Date, Heure))
Y_train = df$Conso[337:52561]

X_test = subset(df[105216:121248,], select = -c(Conso, ConsoT.1, Date, Heure))
Y_test = df$Conso[105216:121248]

###Expert Construction
#Random Forest
expert_rf <- randomForest(x=X_train, y=Y_train, ntree=100, maxnodes=5)
expert_rf_forecast <- predict(expert_rf, newdata=X_test)

#TSLM
ts <- ts(Y_train, frequency = 48)
expert_tslm <- tslm(ts ~ tod+tow+Fourier+ConsoJ.1+ConsoJ.7+trend+season, data=X_train)
pred <- forecast(expert_tslm, newdata = X_test)
expert_tslm_forecast <- pred$mean


#Gradient Boosting
expert_gbm <- gbm.fit(x=X_train, y=Y_train, n.trees=1000, distribution="gaussian", shrinkage=0.01)
expert_gbm_forecast <- predict(expert_gbm, newdata = X_test)


###Aggregation
experts <- cbind(expert_rf_forecast, expert_tslm_forecast, expert_gbm_forecast)
colnames(experts) <- c("rf", "tslm", "gbm")
or <- oracle(Y_test, experts, model = "convex", loss.type = "square")

rmse_exp <- apply(experts, 2, function(x){sqrt(mean((x - Y_test)^2))})
rmse_exp %>% round(, digits = 0) %>% sort

#Valeur Théorique
M <- mean((Y_train - X_train$ConsoJ.7)^2, na.rm = T)
learning.rate <- (1/M) * sqrt(8*log(ncol(experts))) / length(Y_test)


agg.online_theoric<- mixture(Y = Y_test, 
                             experts = experts,
                             model = 'EWA', 
                             loss.type = "square",
                             loss.gradient = F,
                             parameter=list(eta=learning.rate))

plot(agg.online_theoric)
summary(agg.online_theoric)