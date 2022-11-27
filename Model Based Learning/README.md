# Package EMout

**Authors : Tom Djaaleb & Hugo Attali**

*Ce travail a été réalisé dans le cadre du projet du cours "Model Based Learning" du Master 2 MALIA de l'Université Lyon 2*

> Package requis : numpy, scipy, matplotlib

L'objectif de l'algorithme EMout est de proposer un modèle de mélange capable de détecter les outliers pour un problème de clustering. Si l'algorithme ne détecte pas d'outliers, alors le modèle sera un mélange de $k$ gaussiennes. En revanche, si l'algorithme détecte des outliers, alors le modèle sera un mélange de $k$ gaussiennes et d'une loi uniforme représentant la distribution des outliers.

## La fonction $\texttt{EM}$

La fonction requiert 4 paramètres en entrée : les données ( $\texttt{data}$ ), le nombre de clusters ( $\texttt{clusters}$ ), le nombre d'itération pour chaque algorithme EM ( $\texttt{iter}$ ) et le nombre d'initilisation aléatoire pour les paramètres du modèle ( $\texttt{init}$ ).

La fonction renvoit en sortie un objet de classe $\texttt{Model}$ .

## La classe $\texttt{Model}$

La classe $\texttt{Model}$ possède 7 instances et 2 méthodes

### Instances

$\texttt{Model.data}$ : renvoie les données.

$\texttt{Model.uniform}$ : renvoie $\texttt{False}$ si le modèle ne contient pas d'outliers, $\texttt{True}$ sinon.

$\texttt{Model.tik}$ : renvoie les probabilités de chaque données d'appartenir à chaque classe.

$\texttt{Model.clusters}$ : renvoie le cluster associé à chaque observation.

$\texttt{Model.log\\_likelihood}$ : renvoie la valeur de la *log likelihood* à chaque itération.

$\texttt{Model.bic}$ : renvoie la valeur du critère BIC pour le modèle choisi.

$\texttt{Model.params}$ : renvoie les paramètres du modèle.

### Méthodes

$\texttt{Model.plot()}$ : 

$\texttt{Model.Model.plot\\_llh}$ : trace l'evolution de la *log likelihood* (si celle-ci est constante, alors l'initialisation avait déjà convergé).
