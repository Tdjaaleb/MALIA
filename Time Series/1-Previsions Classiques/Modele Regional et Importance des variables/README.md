# Modele Regional et importance des variables
Dans cette partie, nous testons l'importance des variables et notamment celle de la température et de la consommation à $t-1$ sur les prévisions par région.

Nous reprenons le Gradient Boosting comme modèle et choisissons de changer les paramètres pour réduire le temps d'éxécution :
- Learning rate : 0.1
- Profondeur max : 5 (pas de changement)
- Nombre d'estimateurs : 100

## Modèle Regional avec Température et Conso $t-1$
Dans tous les modèles, la Consommation à $t-1$ est la variable la plus importante (environ 0.99 de score). Quant à la température, celle-ci n'est pas vraiment utile pour la prédiction et est plutôt là pour l'affiner.

#### Résultats par région (RMSE)

| Aura          | Bourgogne     | Bretagne      | Centre        | Grand Est     | Hauts de Fr.  |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 152           | 51            | 144           | 77            | 106           | 127           |

| IDF           | Normandie     | N. Aquitaine  | Occitanie     | PACA          | Pays de Loire |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 234           | 89            | 276           | 114           | 86            | 192           |

Visuellement, les modèles semblent être très performant, malheureusement dans l'optique de prédire à J+1, nous ne pouvons considérer la variable "Conso à $t-1$". Celle-ci peut seulement être efficiente pour prédire un horizon de 1.

## Modèle Regional sans Température et Conso $t-1$
Cette fois-ci, la variable la plus importante est "Conso J-1" (envion 0.75 de score moyen), de plus la variable "Conso J-7" obtient un score honorable d'importance égal à 0.15.

#### Résultats par région (RMSE)

| Aura          | Bourgogne     | Bretagne      | Centre        | Grand Est     | Hauts de Fr.  |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 391           | 153           | 212           | 171           | 305           | 454           |

| IDF           | Normandie     | N. Aquitaine  | Occitanie     | PACA          | Pays de Loire |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 475           | 176           | 411           | 264           | 198           | 282           |

En perdant l'accès à la variable "Conso $t-1$" nous observons une dégradation nette des performances, bien que celle-ci reste toujours bonnes.

## Modèle Regional avec reconstruction de la Conso $t-1$ itérativement (AURA uniquement)
En troisième lieu, nous voulons voir s'il est possible de tirer profit de la prédiction de la consommation au temps $t+1$ pour utiliser cette information pour prédire la consommation au temps $t+2$.
Nous créeons itérativement la variable "Conso $t-1$" en utilisant les prédictions passées de notre modèle.
Malheureusement, nous obtenons pour la région AURA une RMSE de 483 ce qui fait que cette méthode est encore plus mauvaise que la méthode sans la variable "Conso $t-1$". Cette mauvaise performance viens probablement de la diffusion de l'erreur de la prédiction au temps $t+1$ à toutes les prédictions futures.

