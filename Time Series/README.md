# Projet de Time Series Forecasting

**Auteurs du projet : Tom Djaaleb & Hugo Attali**

## Étape numéro 1 : Récupération des données

Nous récupérons les données de consommation d'énergie en France au niveau national et pour les 12 régions du 01/01/2016 au 30/11/2022.
Site : https://www.rte-france.com/eco2mix/telecharger-les-indicateurs

Nous récupérons également les données météo des années 2016 à 2022.
Site : https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=90&id_rubrique=32

## Étape numéro 2 : Preprocessing des données

Nous mettons en forme les données et interpolons les données manquantes à l'aide d'une interpolation cubique.
Nous crééons ensuite des covariables pouvant être utiles à la prédiction.

Nous exportons les données nettoyées dans des fichiers pour les réutiliser plus tard.

## Étape numéro 3 : Prévisions classiques

Dans un premier temps, nous testons les performances de deux modèles sur les données nationales.

Le plus performant des deux modèles est choisi pour le reste de l'étude.

Ensuite nous entraînons 12 modèles avec la méthode la plus performante sur les données nationales (un pour chaque région) et regardons l'importances des différentes covariables.

## Étape numéro 4 : Réconciliation

Dans cette partie, nous testons deux méthodes de réconciliation des données *post-forecasting*. Nous mesurons les performances des deux méthodes.

## Étape numéro 5 : Aggregation

Nous construisons trois modèles experts pour la prévision des données nationales puis aggrégeons les prédictions à l'aide d'un algorithme d'aggrégation sequentielle.

## Étape numéro 6 : Données Covid

Les périodes de confinement étant très probablement particulières, nous avons décidé de ne pas utiliser les années 2020 et 2021 dans notre ensemble d'entraînement. Néanmoins, nous avons voulu tester notre modèle Gradient Boosting pendant le premier confinement (Mars-Avril 2020). Sur cette période, nous obtenons un RMSE de 3131 contre 2537 sur la période Mars-Avril 2022. Notre modèle est donc sensible à des événements inatendus.

## Conclusion et perspective

Notre modèle final est donc un **Gradient Boosting** avec 1000 arbres ayant une profondeur maximum de 5, entraîné avec un *learning rate* de 0.01. Nous préconisons la méthode **Structurally Weighted Least Squares** *post-forecasting* pour la réconciliation entre les prédictions nationales et régionales. La prédiction aggrégée par plusieurs experts ne donne pas des résultats satisfaisants.

Une idée pour la suite qui nous est venue serait de construire une librairie Python pour l'algorithme d'aggrégation séquentielle de plusieurs experts.
