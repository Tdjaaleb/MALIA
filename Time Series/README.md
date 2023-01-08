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
