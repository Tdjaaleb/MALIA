# 3-Aggregation

Dans cette partie, nous réalisons une prédiction aggrégée par plusieurs modèles sur la consommation nationale. Les trois modèles choisis sont :
- Random Forest
- Gradient Boosting
- Time Series Linear Model

Nous voulions initialement inclure un modèle ARIMA dans nos experts mais la complexité d'entraîner ce modèle avec un grand nombre de données et de prédire également un grand nombre de données était trop demandant en temps de calcul et/ou en puissance de calcul.

Dans un premier temps, nous entraînons nos modèles séparemment et calculons la RMSE de chaque modèle. Le meilleur semble être le modèle TSLM.

Nous calculons ensuite la valeur théorique du learning rate pour l'algorithme d'aggrégation.
