# 2-Reconciliation
Dans cette partie, nous souhaitons réconcilier nos prédictions pour que la somme des prévisions par région soit égale à la prévision de la consommation nationale.

Pour ce faire nous utilisons la librairie `scikit-hts` (https://scikit-hts.readthedocs.io/en/latest/readme.html).

Nous choisissons de réconcilier post-forecasting, c'est à dire que nous prédisons chaque série indépendamment et que nous réconcilions les prévisions ensuite.

Les méthodes de réconciliations choisies proviennent de l'article "Optimal Forecast Reconciliation for Hierarchical and Grouped Time Series Through Trace Minimization" de Wickramasuriya, Athanasopoulos et Hyndman (https://www.tandfonline.com/doi/abs/10.1080/01621459.2018.1448825)

Pour mesurer la performance de notre réconciliation, nous calculons la moyenne de l'effet de la réconciliation sur la RMSE de chaque séries :

$\text{metrics}= \frac{1}{13} \sum_{i} \frac{RMSE_r(y,\hat{y}_i^r) - RMSE_b(y,\hat{y}_i^b)}{RMSE_b(y,\hat{y}_i^b)}*100$

Avec $RMSE_r$ la RMSE de la série réconciliées, $RMSE_b$ la RMSE de 

Dans un premier temps, nous testons la méthode *Ordinary Least Squares (OLS)* 
