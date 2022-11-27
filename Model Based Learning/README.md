# Package EMout

** Authors : Tom Djaaleb & Hugo Attali **

*Ce travail a été réalisé dans le cadre du projet du cours "Model Based Learning" du Master 2 MALIA de l'Université Lyon 2*

L'objectif de l'algorithme EMout est de proposer un modèle de mélange capable de détecter les outliers pour un problème de clustering. Si l'algorithme ne détecte pas d'outliers, alors le modèle sera un mélange de $k$ gaussiennes. En revanche, si l'algorithme détecte des outliers, alors le modèle sera un mélange de $k$ gaussiennes et d'une loi uniforme représentant la distribution des outliers.

### La fonction EMout

La fonction requiert 4 paramètres en entrée : les données ( $\texttt{data}$ ), le nombre de clusters ( $\texttt{clusters}$ ), le nombre d'itération pour chaque algorithme EM ( $\texttt{iter}$ ) et le nombre d'initilisation aléatoire pour les paramètres du modèle ( $\texttt{iter}$ ).
