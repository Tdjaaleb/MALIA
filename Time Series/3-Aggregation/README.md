# 3-Aggregation

Dans cette partie, nous réalisons une prédiction aggrégée par plusieurs modèles sur la consommation nationale. Les trois modèles choisis sont :
- Random Forest
- Gradient Boosting
- Time Series Linear Model

Nous voulions initialement inclure un modèle ARIMA dans nos experts mais la complexité d'entraîner ce modèle avec un grand nombre de données et de prédire également un grand nombre de données était trop demandant en temps de calcul et/ou en puissance de calcul.

Dans un premier temps, nous entraînons nos modèles séparemment et calculons la RMSE de chaque modèle :

| RF            | TSLM          | GB            |
| ------------- | ------------- | ------------- |
| 5527          | 2721          | 2826          |

Nous calculons ensuite la valeur théorique du learning rate pour l'algorithme d'aggrégation, puis nous lançons l'algorithme d'optimisation.

Il en ressort que les RF ont un poids négligeable dans la prédiction par rapport aux deux autres modèles. La RMSE de l'aggrégation pondérée est égale à 2830, ce qui n'est pas vraiment convaincant. 

Le fichier `Aggregation.pdf` propose le notebook commenté et exécuté, `Graphiques.pdf` montrent les résultats visuels de l'aggrégation et `Experts predictions.R` est le fichier avec le code brut.
