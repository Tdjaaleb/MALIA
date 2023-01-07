# Choix du modèle
Nous avons décidé de comparer deux modèles pour la prévision de la consommation nationale d'énergie : GradientBoosting et SeriesNet.

# Données
- Train : 01/01/2016 à 31/12/2018
- Validation : 01/01/2019 à 31/12/2019
- Test : 01/01/2022 à 30/11/2022

# Métrique
Le modèle qui obtiendra la plus petite *Root Mean Squared Error* sur les données test sera notre modèle de prévision

# GradientBoosting
Pour déterminer les hyperparamètres de notre modèle, nous effectuons un *Grid Search* avec une 3-*Cross Validation* sur les données d'entraînements (données de validations non utilisées).

Les paramètres choisis sont :
- Learning rate : 0.01
- Profondeur max : 5
- Nombres d'estimateurs : 1000

Nous obtenons une RMSE de **2167.23** sur les données tests.

# SeriesNet
SeriesNet est une architecture de Deep Learing développé par Shen et al. en 2018. Elle combine une couche LSTM et un réseau *Dilated Causal Convolution* avec *Deep Residuals*.
Les paramètres sont les mêmes que dans l'article.

Pour effectuer l'entraînement du modèle, nous choisissons de lancer l'entraînement sur 5000 époques et de mettre un terme à celui-ci lorsqu'il n'y a pas eu d'amélioration sur la RMSE de l'ensemble de validation sur les 200 dernières époques.

Nous obtenons une RMSE de **2270.85** sur les données tests.

### Notre modèle pour la suite sera donc le GradientBoosting
