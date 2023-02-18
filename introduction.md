# Membres de l'équipe
Jonas Gabirot
Dereck Piché (matricule 20177385)
Guillermo Martinez 


# Brève description du projet

Différentes séquences d’ADN ont tendances à se plier dans une repliement 3-dimensionnel
qui leur est propre. Il existe un service (NUPACK)qui utilise des algorithmes classiques (sans apprentissage automatique)
afin de déterminer l’énergie libre qui sera contenue dans la séquence suite à son repliement. Notre tache sera d’utiliser 
des réseaux de neurones profonds spécialisés dans le traitement de séquences (RNN, LSTM, Transformers) afin d’apprendre 
automatique les principes sous-jacents à ces processus en utilisant NUPACK pour obtenir un ensemble d’entrainement. 

Motivation de Dereck:
J’aimerais augmenter ma familiarité avec l’utilisation d’algorithmes d’apprentissage
automatique spécialisés dans le traitement de séquences (RNN, LSTM, Transformers). 
De plus, je me suis découvert un intérêt récent dans la biologie. De plus, c’est l’algorithme 
AlphaFold de DeepMind qui m’a fait comprendre la puissance des réseaux de neurones alors 
je suis excité de travailler sur un projet connexe.


# Étapes prévues
## Étude des concepts
Nous devons commencer par appronfondire notre compréhension du sujet suite à la séance au MILA avec Alex et insert.
## Création (ou obtention) de base de donnée NUPACK.
Nous utiliserons cette base de donnée pour entrainer
notre modèle.
## Étude des modèles
Faire une étude des modèles RNN et des Transformers afin d'établir notre méthodologie.
## Choix de méthodologie
Choix des hyperparamètres, choix de la taille et des caractéristiques des données et choix des modèles utilisés.

## Implémentation
Implémentation des algorithmes en utilisant la librairie 
Pytorch avec Python.

## Objectif 
Obtenir un modèle qui est capable de reproduire qui généralise bien sur des prédictions NUPACKà. Ainsi, on cherche à obtenir un modèle qui performe bien sur des 
exemples qui n'ont pas été utilisés pour l'entrainement.


# Répartition du travail
Chacun des membres contribuera à toutes les parties, mais 
voici les concentrations particulières des membres de l'équipe (il est fortement probable que cette répartiton sous sujette à des changements alors que le projet avance)
Guillermo 
Concentration sur la biologie.
Dereck 
Concentration sur la théorie derrière les modèles d'apprentissage automatique utilisés.
Jonas
Concentration sur l'implémentation.

