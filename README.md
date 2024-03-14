# Astraios : Python deorbit computing

Astraios est une bibliothèque Python conçue pour faciliter le calcul d'orbites et la simulation de la désorbitation de satellites en orbite autour de la Terre. Cette bibliothèque fournit des fonctionnalités pour la modélisation des orbites elliptiques, la réalisation de manoeuvres orbitales, le calcul des paramètres d'orbite et la simulation de la désorbitation de satellites.

## Installation

Vous pouvez installer Astraios en utilisant pip. Assurez-vous d'avoir Python d'installé.


```pip install https://github.com/Timotraque/MGA802_projet```

## Dépendances

Astraios a besoin des bibliothèques suivantes :

- pandas
- matplotlib
- openpyxl

Elles peuvent être installées automatiquement à l'aide de la commande :  
``pip install -r requirements.txt``

## Utilisation
Un exemple d'utilisation est fourni dans le fichier main.py. Il permet de créer une orbite, de l'afficher et 
d'effectuer des manoeuvres orbitales. En définissant les paramètres d'un satellite, il est également possible de calculer
sa durée de vie en orbite.

### Objet SpaceBody :
Le premier objet de cette librairie est 
L'objet `SpaceBody` est une classe de base utilisée dans la bibliothèque Astraios pour représenter divers corps célestes
tels que les planètes, les satellites et d'autres éléments naturels ou artificiels en orbite. Cette classe contient 
notamment un argument `mass` qui représente la masse du corps. Seuls les corps célestes de type 'SpaceBody' peuvent utiliser 
la méthode Two_body_problem().

#### Planet
La sous-classe `Planet` hérite de `SpaceBody` et est utilisée pour représenter spécifiquement une planète dans le système. 
En plus de la masse héritée, cette classe a des attributs supplémentaires tels que `radius` pour le rayon de la planète 
en mètres et `color` pour la couleur utilisée dans les visualisations.

#### Satellite
La sous-classe `Satellite` hérite également de `SpaceBody` et est utilisée pour représenter un satellite en orbite autour
d'une planète ou d'une autre entité céleste. En plus de la masse héritée, cette classe a des attributs supplémentaires 
tels que `cx` pour le coefficient de traînée sans dimension et `surface` pour la surface transversale du satellite en mètres carrés.
Habituellement, un satellite possède un coefficient de traînée de 2 si il n'a pas été évalué lors de la phase de conception.

### Objet Orbit :

L'objet `Orbit` est une classe centrale dans la bibliothèque Astraios qui permet de modéliser les orbites elliptiques 
autour d'un corps céleste, tel que la Terre. Cette classe est utilisée pour définir les paramètres d'une orbite, effectuer
des manoeuvres orbitales et simuler la désorbitation d'un satellite. Toute étape du programme nécessitant des calculs (trajectoire,
vitesse) doit utiliser cet objet et ces méthodes.

#### init()
Le constructeur de la classe `Orbit` permet d'initialiser un objet orbite avec les paramètres spécifiés :
- `perigee` : Altitude du périgée en mètres.
- `apogee` : Altitude de l'apogée en mètres.
- `inclinaison` : Inclinaison de l'orbite en degrés (par défaut 0).
- `dt` : Intervalle de temps pour la simulation en secondes (par défaut 1000).
- `temps_simu` : Durée de la simulation en secondes (par défaut 800000).

#### plot_orbit()
Cette méthode permet de tracer l'orbite elliptique dans un système de coordonnées tridimensionnel. Elle affiche également le périgée et l'apogée de l'orbite.

#### manoeuvre()
La méthode `manoeuvre` permet d'effectuer une manoeuvre orbitale en modifiant la vitesse orbitale du satellite. Les paramètres de la manoeuvre sont spécifiés comme suit :
- `delta_v` : Changement de vitesse en mètres par seconde.
- `direction` : Direction de la manoeuvre ('prograde', 'retrograde' ou 'radiale').
- `position` : Position de la manoeuvre ('perigee' ou 'apogee').

#### desorbitation()
La méthode `desorbitation` simule la désorbitation du satellite en orbite. Elle calcule la trajectoire du satellite en tenant compte de la force gravitationnelle, de la traînée atmosphérique et éventuellement d'une propulsion supplémentaire. Les paramètres de la désorbitation sont spécifiés comme suit :
- `satellite` : Instance de la classe `Satellite` représentant le satellite en orbite.
- `position` : Position de la manoeuvre de désorbitation ('perigee' ou 'apogee').
- `atmosphere` : Instance de la classe `Atmosphere` représentant l'atmosphère terrestre.
- `plot_orbit` : Optionnel, si True, affiche la trajectoire du satellite en orbite (par défaut False).
- `force_propulsion` : Optionnel, force de propulsion supplémentaire en newtons (par défaut 0).


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

# Bibliographie :

https://kp.gfz-potsdam.de/en/data#c222

