# Preprocessing

Dans un premier temps, nous récupérons toutes les données et interpolons les données manquantes avec une interpolation cubique.

Ensuite nous crééons de nouvelle covariables :

- *Conso T-1* : la consommation à la période précédente
- *Conso J-1* : la consommation 24h avant
- *Conso J-7* : la consommation 7 jours avant
- *tod* : valeur comprise entre 0 et 1, indiquant la période de la journée
- *tow* : valeur comprise entre 0 et 1, indiquant le jour de la semaine
- *Fourier* : La série débruitée avec la transformé de Fourier (cela s'apparente grossièrement à la période de l'année)
