# Ce fichier contient les constantes de la librairie
from enum import Enum

mu_terre = 3.986e14  # Paramètre gravitationnel standard de la Terre en m^3/s^2
rayon_terre = 6.371e6  # Rayon moyen de la Terre [m]

class Type_manoeuvre(Enum):
    prograde = 'prograde',
    retrograde = 'retrograde',
    radiale = 'radiale'

class Position_manoeuvre(Enum):
    apogee = 'apogee',
    perigee = 'perigee'