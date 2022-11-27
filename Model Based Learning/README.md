# Package EMout

**Authors : Tom Djaaleb & Hugo Attali**

*Ce travail a été réalisé dans le cadre du projet du cours "Model Based Learning" du Master 2 MALIA de l'Université Lyon 2*

> Packages requis : numpy, scipy, matplotlib

L'objectif de l'algorithme EMout est de proposer un modèle de mélange capable de détecter les outliers pour un problème de clustering. Si l'algorithme ne détecte pas d'outliers, alors le modèle sera un mélange de $k$ gaussiennes. En revanche, si l'algorithme détecte des outliers, alors le modèle sera un mélange de $k$ gaussiennes et d'une loi uniforme représentant la distribution des outliers.

## Utilisation du package

### Sur Google Colab

`import os`

`ROOT_DIR = os.path.abspath("/content")`

`os.chdir(ROOT_DIR)`

`!git clone https://github.com/Tdjaaleb/MALIA`

`os.chdir("MALIA/Model Based Learning")`

`from EMout import EM`

### En local

Il faut télécharger le *repository* à l'adresse suivante https://github.com/Tdjaaleb/MALIA puis extraire le fichier *EMout.py*. Il faut ensuite copier ce fichier dans le repertoire de travail. Enfin il suffit d'importer la fonction.

`from EMout import EM`


## La fonction $\texttt{EM}$

La fonction requiert 4 paramètres en entrée : les données ( $\texttt{data}$ ), le nombre de clusters ( $\texttt{clusters}$ ), le nombre d'itération pour chaque algorithme EM ( $\texttt{iter}$ ) et le nombre d'initilisation aléatoire pour les paramètres du modèle ( $\texttt{init}$ ).

La fonction entraîne deux modèles : un modèle à $k$ gaussiennes et un modèle à $k$ gaussiennes + une uniforme avec l'algorithme EM. Le modèle ayant le critère BIC le plus élevé est choisi et renvoyé par la fonction.

La fonction renvoit en sortie un objet de classe $\texttt{Model}$ .

**Disclaimer : il est parfois nécessaire de relancer la fonction plusieurs fois car il arrive que celle-ci converge vers un mauvais maxima. De plus il est possible qu'un message d'erreur apparaisse si des points sont trop éloignés, ceci est dû à la fonction $\texttt{scipy.stats.multivariate\_normal.pdf()}$ qui renvoit parfois des 0 car la valeur est inférieure à 10^-16.

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

$\texttt{Model.plot()}$ : projette les points en deux dimensions et les colore selon leur appartenance aux clusters.

$\texttt{Model.Model.plot\\_llh()}$ : trace l'evolution de la *log likelihood* (si celle-ci est constante, alors l'initialisation avait déjà convergé).

## Exemple

Un exemple d'utilisation est proposé dans le fichier *Example.ipynb*
