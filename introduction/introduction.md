# Membres de l'équipe
Jonas Gabirot (matricule 20185863)
Dereck Piché (matricule 20177385)
Guillermo Martinez (matricule 20076854)


# Brève description du projet

Les aptamères sont des petites séquences monocaténaires d’acide désoxyribonucléique (ADN) qui sont communément utilisés en tant que senseurs pour tracer la propagation de diverses molécules dans leur environnement, tel que des antibiotiques, des neurotransmetteurs et de l’adénosine triphosphate (ATP). Récemment, les « aptasenseurs » ont été proposés comme traceurs potentiels du mouvement des molécules dans des milieux denses tels que le sang ou les eaux polluées. Bien que plusieurs candidats aient été proposés, l’enjeu demeure d’identifier la relation causale entre la composition des séquences d’aptamères et leur performance comme senseurs pour une molécule donnée. Cette relation causale entre séquence et performance s’explique principalement par la structure 3 dimensionnelle des séquences d’aptamères. Cette structure est responsable d’initier et de soutenir la liaison des apatamères aux molécules cibléess en fonction de sa stabilité respective.

Plusieurs avancées en intelligence artificielle, plus particulièrement en apprentissage profond, permettent désormais l’apprentissage automatique de la fonction de « free energy » des séquences d’aptamères. Grâce à la plateforme E2EDNA, qui utilise les librairies « NUPACK » et « seqfold », nous allons en premier lieu échantillonner des séquences unidimensionnelles d’aptamères d’une longueur de 10 à 30 composantes, ainsi que leur niveau de « free energy » tel qu’indiqué dans la librairie NUPACK, et puis entraîner un réseaux neuronal récurrent et un transformer à prédire le « free energy » des séquences en fonction de la modélisation du pliage tridimensionnel des aptamères simulé par la plateforme E2EDNA à une température donnée. L’apprentissage de la fonction de « free energy » des séquences d’aptamères viendra automatiser, et par conséquent, accélérer la prédiction de la stabilité d’aptasenseurs potentiels pour tracer le mouvement des molécules dans des nouveaux milieux intéressants et prometteurs.

Si le temps le permet, ce projet abrodera dans un deuxième lieu la génération de proto séquences d’aptasenseurs possédant les caractéristiques associées à une faible « free energy », et donc, à une forte stabilité, selon les prédictions des modèles que nous aurons entraînés. La stabilité des séquences les plus performantes que nous aurons générés seront par la suite validées sur d’autres plateformes que l'E2EDNA. Si ces diverses plateformes convergent sur une forte stabilité potentielle pour certaines de nos séquences générées, ces proto-aptamères seront des candidats potentiels à être synthétisés par des laboratoire dans le but de tester objectivement leur validité externe dans des problèmes concrets tels que le traçage de polluants dans les océans.   

**Ajouter les informations nécessaires des paragraphes d'en bas dans le pragraphe en haut, effacer le rest (pour la description)**

Différentes séquences d’ADN ont tendances à se plier dans une repliement 3-dimensionnel
qui leur est propre. Il existe un service (NUPACK) qui utilise des algorithmes classiques (sans apprentissage automatique)
afin de déterminer l’énergie libre qui sera contenue dans la séquence suite à son repliement. Notre tache sera d’utiliser 
des réseaux de neurones profonds spécialisés dans le traitement de séquences (RNN, LSTM, Transformers) afin d’apprendre 
automatiquement les principes sous-jacents à ces processus en utilisant NUPACK pour obtenir un ensemble d’entrainement. 

Motivation:

Dereck: J’aimerais augmenter ma familiarité avec l’utilisation d’algorithmes d’apprentissage
automatique spécialisés dans le traitement de séquences (RNN, LSTM, Transformers). 
C’est l’algorithme AlphaFold de DeepMind qui m’a fait comprendre la puissance des réseaux de neurones alors 
je suis excité de travailler sur un projet connexe. De plus, je me suis découvert un intérêt récent dans la biologie.

Jonas: J'ai aussi été inspiré par AlphaFold de DeepMind. Ce modèle m'a fait comprendre que l'apprentissage machine peut avoir un impact concret et important pour la recherche scientifique, en particulier en biologie. Le monde de la biologie est vaste, ce qui le rend difficile à explorer par la recherche exhaustive, c'est donc un domaine parfait pour les algorithmes d'IA. C'est aussi le cas pour les aptamères, donc ce projet est une bonne opportunité d'apprendre à implémenter des algorithmes complexes tout ayant un impact réel sur un domaine scientifique émergent.

Guillermo: Selon le principe de "free energy" tel que formulé par Karl Friston, la diminution du free energy est la fonction objective en vigeur de laquelle tout ce qui existe, existe. Mieux comprendre la formulation de ce principe grâce à des outils mathématiques et algorithmes est devenu un des mes intérêts principaux. De plus, ce projet me permettra d'entraîner des réseaux de neurones avec des données séquentielles, mon format favori d'information, pour ensuite acquérir du hands-on experience à générer des séquences qui optimisent la diminution du free energy à l'aide de GFlowNets. À long terme, je crois que ce travail sur la diminution du free energy contribuera significative dans l'ingénérie de la conscience chez des machines. 

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

Guillermo : Bien comprendre les enjeux de cette recherche grâce à une revue de litérature approfondie, fine-tuning de l'architecture et des hyperparamètres des réseaux de neurones, génération de nouvelles séquences grâce à des GFlowNets. 

Dereck : 
Concentration sur la théorie derrière les modèles d'apprentissage automatique utilisés.

Jonas : 
Concentration sur l'implémentation.

