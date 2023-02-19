# Membres de l'équipe
Jonas Gabirot (matricule 20185863)
Dereck Piché (matricule 20177385)
Guillermo Martinez 


# Brève description du projet

Différentes séquences d’ADN ont tendances à se plier dans une repliement 3-dimensionnel
qui leur est propre. Il existe un service (NUPACK) qui utilise des algorithmes classiques (sans apprentissage automatique)
afin de déterminer l’énergie libre qui sera contenue dans la séquence suite à son repliement. Notre tache sera d’utiliser 
des réseaux de neurones profonds spécialisés dans le traitement de séquences (RNN, LSTM, Transformers) afin d’apprendre 
automatiquement les principes sous-jacents à ces processus en utilisant NUPACK pour obtenir un ensemble d’entrainement. 

Motivation de Dereck:
J’aimerais augmenter ma familiarité avec l’utilisation d’algorithmes d’apprentissage
automatique spécialisés dans le traitement de séquences (RNN, LSTM, Transformers). 
De plus, je me suis découvert un intérêt récent dans la biologie. De plus, c’est l’algorithme 
AlphaFold de DeepMind qui m’a fait comprendre la puissance des réseaux de neurones alors 
je suis excité de travailler sur un projet connexe.

Motivation de Jonas:
J'ai aussi été inspiré par AlphaFold de DeepMind. Ce modèle m'a fait comprendre que l'apprentissage machine peut avoir un impact concret et important pour la recherche scientifique, en particulier en biologie. Le monde de la biologie est vaste, ce qui le rend difficile à explorer par la recherche exhaustive, c'est donc un domaine parfait pour les algorithmes d'IA. C'est aussi le cas pour les aptamères, donc ce projet est une bonne opportunité d'apprendre à implémenter des algorithmes complexes tout ayant un impact réel sur un domaine scientifique émergent.

# Étapes prévues
## Étude des concepts
Nous devons commencer par appronfondir notre compréhension du sujet suite à la séance au MILA avec Alex et Mélisande.
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
Obtenir un modèle qui est capable de reproduire qui généralise bien sur des prédictions NUPACK. Ainsi, on cherche à obtenir un modèle qui performe bien sur des 
exemples qui n'ont pas été utilisés pour l'entrainement.
Si cette première étape est réussite, un objectif secondaire est de générer des nouveaux aptamères avec des énergies libres spécifiques, avec un algorithme comme GAN ou GFlowNet


# Répartition du travail
Chacun des membres contribuera à toutes les parties, mais 
voici les concentrations particulières des membres de l'équipe (il est fortement probable que cette répartiton sous sujette à des changements alors que le projet avance)

Guillermo : Concentration sur la biologie.

Dereck : 
Concentration sur la théorie derrière les modèles d'apprentissage automatique utilisés.

Jonas : 
Concentration sur l'implémentation.

