# Fichier main.py principal du projet

import math

# Définition des constantes
Re = 6378000  # Earth radius in meters
Me = 5.98E+24  # Earth mass in kg
G = 6.67E-11  # Gravitational constant
pi = 3.1416
dT = 0.1  # Time increment in days
D9 = dT * 3600 * 24  # Time increment in seconds

# Fonction pour calculer la période orbitale en secondes
def orbital_period(R):
    return 2 * pi * math.sqrt(R ** 3 / Me / G)

# Fonction pour calculer la décroissance orbitale
def orbital_decay(H, F10, Ap, A, M, R):
    SH = (900 + 2.5 * (F10 - 70) + 1.5 * Ap) / (27 - 0.012 * (H - 200))
    DN = 6E-10 * math.exp(-(H - 175) / SH)  # Atmospheric density
    dP = 3 * pi * A / M * R * DN * D9  # Decrement in orbital period
    return dP

# Fonction pour afficher les informations formatées
def print_info(T, H, P, MM, Decay):
    print(f"{T:.1f} {H:.1f} {P / 60:.1f} {MM:.4f} {Decay:.2f}")

# Entrée des paramètres
N = input("Nom du satellite : ")
M = float(input("Masse du satellite (kg) : "))
A = float(input("Surface du satellite (m^2) : "))
H = float(input("Altitude initiale (km) : "))
F10 = float(input("Flux solaire radio (SFU) : "))
Ap = float(input("Indice géomagnétique A : "))

# Initialisation des variables
T = 0
H2 = H
R = Re + H * 1000  # Orbital radius in meters
P = orbital_period(R)  # Orbital period in seconds

# Impression des informations
print("SATELLITE ORBITAL DECAY - Model date/time ")
print("Satellite -", N)
print(f"Mass = {M:.1f} kg")
print(f"Area = {A:.1f} m^2")
print(f"Initial height = {H:.1f} km")
print(f"F10.7 = {F10} Ap = {Ap}")

# En-tête des colonnes
print("TIME HEIGHT PERIOD MEAN MOTION DECAY")
print("(jours) (km) (mins) (rev/day) (rev/day^2)")

# Boucle de calcul et d'impression
while True:
    dP = orbital_decay(H, F10, Ap, A, M, R)
    if H <= H2:
        Pm = P / 60
        MM = 1440 / Pm
        Decay = dP / dT / P * MM
        print_info(T, H, P / 60, MM, Decay)
        H2 -= 10
    if H < 180:
        break
    P -= dP
    T += dT
    R = (G * Me * P * P / (4 * pi * pi)) ** (1 / 3)
    H = (R - Re) / 1000

# Durée de vie estimée du satellite
print(f"Re-entry after {T:.0f} days ({T / 365:.2f} years)")
