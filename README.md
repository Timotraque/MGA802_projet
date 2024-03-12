# MGA802_projet : 

Ce dépot GitHub conttient une librairie permettant de modéliser la trajectoire de satellites ainsi que les manoeuvres spatiales pouvant être réalisées en s'appuyant sur les équations de mécanique orbitale.  
Un fichier main.py contient un exemple d'utilisation tandis que le fichier classe_orbite renferme les outils nécessaires.

### Definition du projet de MGA802

# ***<p width style="text-align: center;">Concepteur de mission spatiale</p>***

# Objectifs :
- Visualiser une orbite autour de la Terre ou de la Lune.
- Visualiser une ou plusieurs manoeuvres autour de la Terre ou entre la Terre et la Lune.
- Résoudre les équations de transfert orbital
- Visualiser des orbites de missions spatiales dont les caractéristiques sont en accès libre sur internet

# Etude de l'existant : 
- La bibliothèque "poliastro" permet de résoudre certain problèmes usuels d'astrodynamique, elle a été développée par 
Juan Luis Cano Rodríguez et Jorge Martínez Garrido, ingenieurs. Les resultats de leurs travaux ont été présentés lors de 
la 21e conférence PYTHON IN SCIENCE (SCIPY 2022) DOI: 10.25080/majora-212e5952-015
- "Journey" est une plateforme de conception de mission spatial développée par la compagnie Morpheus Space, seule la
phase de conception préliminaire de mission est pour l'instant disponible à l'achat.
- La NASA propose également une suite d'add-ons pour MatLab dont 'General Mission Analysis Tool', il permet la visualisation
en trois dimensions d'orbites et de cones de distribution de signaux diffusés par des antennes :  

<p align="center">
<img src="https://a.fsdn.com/con/app/proj/gmat/screenshots/GMAT_OFI_FOV.png/max/max/1" width="400" align="center"/> </p>

- Des données publiques de nombreuses missions spatiales sont publiées par la NASA ou l'ESA. Parmis celles-ci des
données de trajectoires sont disponibles à l'adresse : https://data.nasa.gov/browse?q=trajectory%20data&sortBy=relevance

# Demarche :  
### Visualisation : 
L'utilisation d'objets de classe *orbite* dont les paramètres seraient connus car issus de données ou demandées à l'utilisateur
(console ou **YAML**) peut permettre de rassembler les données définissant une trajectoire autour d'un astre.
Les fonctions d'affichage ``orbit_plotter()`` devraient pouvoir afficher les orbites associées (en deux dimensions dans
un premier temps) 
### Importation de données :
Des données issues de la NASA, de l'ESA ou de toute autre source fiable peuvent être importées, soit à travers des requêtes
soit manuellement. Elles seront traitées et filtrées afin de permettre leur exploitation par la partie **Visualisation**.

### Traitement :
Le calcul de caractéristiques de trajectoire peut être réalisé à la demande de l'utilisateur selon des critères qu'il défini ou désire obtenir (périgée, apogée, vitesse etc...).  
Le calcul de manoeuvre doit être réalisé à partir d'un objectif défini (altitude, excentricité, inclinaison etc...). Il
doit permettre de définir le nombre de manoeuvres, l'orientation du (ou des) changements de vitesse, leur position sur
les différentes orbites de transfert, le temps estimé de manoeuvre et la quantité de Delta V nécessaire au succès de la mission.  
Les calculs réalisés s'appuieront sur les lois de Kepler ainsi que les lois usuelles de mécanique orbitale (2 bodies problem, 3 bodies problem etc...)
dont la résolution pourra s'appuyer sur des bibliothèques comme NumPy ou SciPy.
