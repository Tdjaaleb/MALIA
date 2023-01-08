# 2-Reconciliation
Dans cette partie, nous souhaitons réconcilier nos prédictions pour que la somme des prévisions par région soit égale à la prévision de la consommation nationale.

Pour ce faire nous utilisons la librairie `scikit-hts` (https://scikit-hts.readthedocs.io/en/latest/readme.html).

Nous choisissons de réconcilier post-forecasting, c'est à dire que nous prédisons chaque série indépendamment et que nous réconcilions les prévisions ensuite.

Les méthodes de réconciliations choisies proviennent de l'article "Optimal Forecast Reconciliation for Hierarchical and Grouped Time Series Through Trace Minimization" de Wickramasuriya, Athanasopoulos et Hyndman (https://www.tandfonline.com/doi/abs/10.1080/01621459.2018.1448825)

Pour mesurer la performance de notre réconciliation, nous calculons la moyenne de l'effet de la réconciliation sur la RMSE de chaque série :

$\text{metric}= \frac{1}{13} \sum_{i} \frac{RMSE_r(y_i,\hat{y}_i^r) - RMSE_b(y_i,\hat{y}_i^b)}{RMSE_b(y_i,\hat{y}_i^b)}*100$

Avec $RMSE_r$ la RMSE de la série réconciliée et $\hat{y}_i^r$ la prédiction réconciliée, $RMSE_b$ la RMSE de la série prédite indépendemment et $\hat{y}_i^b$ la prédiction de la série indépendante. Nous divisons ensuite la somme par 13 (Nationale + 12 régions).
Le modèle qui obtient la plus petite *metric* est considéré comme étant le plus performant. A noté que cette métrique est fortement dépendante de $\hat{y}_i^b$ et donc des modèles entraînés.

### *Ordinary Least Squares (OLS)*
Avec cette méthode nous obtenons une variation moyenne de la RMSE de 2.52%.

### *Structurally Weighted Least Squares (WLSS)*
Avec cette méthode nous obtenons une variation moyenne de la RMSE de 0.29%.

Ces résultats sont valides pour les modèles entraînés dans le notebook. En effectuant plusieurs exécutions nous obtenons des résultats différents, mais la méthode WLSS semble toujours être plus performante que la méthode WLSS.
