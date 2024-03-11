import pdb

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle
from mpl_toolkits.mplot3d import art3d
from constantes import *
import pandas as pd
import math

class SpaceBody():

    """Define a body enrolled in an orbit,
    it can be a planet, a star, a satellite or any kind of artificial or natural element
    """
    def __init__(self, mass=0):
        self.mass = mass


class Planet(SpaceBody):

    def __init__(self,mass, radius=0,color='b'):
        super().__init__(mass)
        self.radius = radius    # [m]
        self.color = color


class Satellite(SpaceBody):
    def __init__(self, mass, surface, cx=2):
        super().__init__(mass)
        self.cx = cx                # [sans dimension]
        self.surface = surface      # [m²]

class Two_body_problem():

    def __init__(self, corps_a, corps_b, rayon=0, excent=0):
        self.corps_a = corps_a
        self.corps_b = corps_b
        self.rayon = rayon
        self.excent = excent

    def show(self):

        # Position centrée de la planete dans le plan orbital
        position_planete_a = (0, 0)
        position_planete_b = (0, self.rayon)
        # Creation de la figure
        fig, ax = plt.subplots()

        # Cercle de la planete
        cercle_planete_a = plt.Circle(position_planete_a, self.corps_a.radius, color=self.corps_a.color)
        cercle_orbite = plt.Circle(position_planete_a, self.rayon, color='k',fill=False)
        cercle_planete_b = plt.Circle(position_planete_b, self.corps_b.radius, color=self.corps_b.color)
        # Ajout de la planete sur la figure

        ax.add_patch(cercle_orbite)
        ax.add_patch(cercle_planete_a)
        ax.add_patch(cercle_planete_b)

        plt.xlim(xmin=-2 * self.rayon, xmax=2 * self.rayon)
        plt.ylim(ymin=-2 * self.rayon, ymax=2 * self.rayon)



        ax.axis("equal")
        plt.show()
        #import pdb; pdb.set_trace()


class Atmosphere:
    def __init__(self):
        self.temperature = self.calculer_temperature()
        self.densite = self.calculer_densites()

    def calculer_densite_air(self, altitude):
        altitude = altitude - rayon_terre
        if altitude < 100000:
            # Constantes de l'atmosphère standard
            p0 = 101325  # Pression atmosphérique au niveau de la mer en Pa
            T0 = 288.15  # Température au niveau de la mer en K
            L = 0.0065  # Variation de température avec l'altitude en K/m
            R = 8.31447  # Constante des gaz parfaits en J/(mol*K)
            M = 0.0289644  # Masse molaire de l'air en kg/mol
            g = 9.80665  # Accélération gravitationnelle en m/s^2

            # Calcul de la température à l'altitude donnée
            T = T0 - L * altitude

            # Calcul de la pression à l'altitude donnée
            p = p0 * np.float_power((1 - ((L * altitude) / T0)), g * M / (R * L))


            # Calcul de la densité de l'air à l'altitude donnée
            rho = p * M / (R * T)
            rho = rho.item()


        elif altitude >= 100000:
            m = 27 - 0.012 * ((altitude / 1000) - 200)

            # En utilisant la temperature en très haute atmosphère
            H = self.temperature / m   # [km]

            rho = 6 * (1 / np.power(10, 10)) * np.exp(-((altitude / 1000) - 175) / H)       # [kg / m3]
            rho = rho.item()

        return rho

    def calculer_densites(self):
        altitude_max = int(1000000)  # 1000 km en mètres
        intervalle = 1000  # Intervalle en mètres
        densites_air = [self.calculer_densite_air(altitude) for altitude in
                        range(0, altitude_max + intervalle, intervalle)]

        return densites_air

    def calculer_temperature(self, annee=2023, mois=4, jour=1, heure=0.0):
        fichier_f10_7 = pd.read_excel('./flux_solaire_data.xlsx')
        f_10_7 = float(fichier_f10_7[(fichier_f10_7['Année'] == annee) & (fichier_f10_7['Mois'] == mois)]['Flux ajusté'])   # [W.m-2.Hz-1]

        fichier_Ap = pd.read_excel('./geomagnetic_data_gfz.xlsx')
        Ap = float(fichier_Ap[(fichier_Ap['year'] == annee) & (fichier_Ap['month'] == mois) & (fichier_Ap['day']==jour) & (fichier_Ap['hour_h']==heure)]['ap'])

        T = 900 + 2.5 * (f_10_7 - 70) + 1.5 * Ap    # [K]

        return T

class Orbite():

    def __init__(self, perigee, apogee, inclinaison=0, dt=10, temps_simu=800000):
        if perigee <= apogee:
            self.perigee = perigee
            self.apogee = apogee
            self.dt = dt
            self.inclinaison = inclinaison
            self.temps_simu = temps_simu
            self.erreur = False
            self.a = (perigee + apogee + 2 * rayon_terre) / 2       # [m] demi grand-axe

        else:
            print("Echec, l'altitude de périgée doit être inférieure à l'apogée")
            self.erreur = True

    def plot_orbit(self):
        if not self.erreur:

            # Calcul de l'excentricité de l'orbite
            eccentricity = (self.apogee - self.perigee) / (self.apogee + self.perigee + 2 * rayon_terre)

            # Calcul de l'angle de l'inclinaison en radians
            inclination_rad = np.radians(self.inclinaison)

            # Générer des angles de 0 à 2pi pour tracer l'orbite
            angles = np.linspace(0, 2 * np.pi, 1000)

            # Calcul des coordonnées polaires
            r = self.a * (1 - eccentricity ** 2) / (1 + eccentricity * np.cos(angles))
            theta = angles

            # Conversion des coordonnées polaires en coordonnées cartésiennes
            x = r * np.cos(theta)
            y = r * np.sin(theta) * np.cos(inclination_rad)
            z = r * np.sin(theta) * np.sin(inclination_rad)

            # Rotation de l'orbite autour de l'axe z pour positionner le périgée
            rotation_angle = np.arctan2(y[0], x[0])
            x, y = x * np.cos(rotation_angle) - y * np.sin(rotation_angle), x * np.sin(rotation_angle) + y * np.cos(rotation_angle)

            # Calcul des coordonnées du périgée et de l'apogée
            x_perigee, y_perigee, z_perigee = self.a * (1 - eccentricity), 0, 0
            x_apogee, y_apogee, z_apogee = -self.a * (1 + eccentricity), 0, 0

            # Création de la figure 3D
            fig = plt.figure(figsize=(8, 8))
            ax = fig.add_subplot(111, projection='3d')

            # Tracer l'orbite
            ax.plot(x, y, z, label='Orbite elliptique')
            ax.scatter(x_perigee, y_perigee, z_perigee, color='blue', label='Périgée')
            ax.scatter(x_apogee, y_apogee, z_apogee, color='red', label='Apogée')

            # Ajouter un cercle représentant une coupe de la surface terrestre dans le plan de l'orbite

            earth_circle = Circle((0, 0), rayon_terre, color='green', alpha=0.3)
            ax.add_patch(earth_circle)
            art3d.pathpatch_2d_to_3d(earth_circle, z=0, zdir="z")

            # Paramètres esthétiques
            ax.set_xlabel('Distance X (km)')
            ax.set_ylabel('Distance Y (km)')
            ax.set_zlabel('Distance Z (km)')
            ax.set_title('Orbite elliptique')
            ax.scatter(0, 0, 0, color='green', label='Terre')
            ax.legend()

            texte_r_perigee = str(self.perigee)
            texte_r_apogee = str(self.apogee)
            texte = f"rayon perigee : {texte_r_perigee}\nrayon apogee : {texte_r_apogee}"
            ax.text(0, 0, s=texte, z=0)

            plt.show()

        else:
            print("Echec, l'altitude de périgée doit être inférieure à l'apogée")

    def manoeuvre(self, delta_v, direction, position):
        # Cette méthode renvoi un objet de type orbite dont les paramètres sont calculés
        # à partir de la manoeuvre executee

        # Calcul de la vitesse orbitale initiale
        match position:
            case Position_manoeuvre.perigee:
                v_initiale = np.sqrt(mu_terre / (self.perigee))

            case Position_manoeuvre.apogee:
                v_initiale = np.sqrt(mu_terre / (self.apogee))

        # Calcul de la variation de vitesse en fonctipon des paramètres de manoeuvre
        match direction:
            case Type_manoeuvre.prograde:
                v_finale = v_initiale + delta_v

            case Type_manoeuvre.retrograde:
                v_finale = v_initiale - delta_v

            # La manoeuvre radiale n'est pas encore codée
            case Type_manoeuvre.radiale:
                new_perigee = self.perigee
                new_apogee = self.apogee

        # Calcul des nouveaux rayons d'orbite
        match position:
            case Position_manoeuvre.perigee:
                r_perigee = self.perigee
                r_apogee = np.power(r_perigee * v_finale, 2) / (2 * mu_terre - r_perigee * np.power(v_finale, 2))

            case Position_manoeuvre.apogee:
                r_apogee = self.apogee
                r_perigee = np.power(r_apogee * v_finale, 2) / (2 * mu_terre - r_apogee * np.power(v_finale, 2))

        # Echange les points de perigee et d'apogee si nécessaire
        if r_apogee < r_perigee:
            dumy = r_apogee
            r_apogee = r_perigee
            r_perigee = dumy

        # Création et retour de la nouvelle orbite
        nouvelle_orbite = Orbite(r_perigee, r_apogee, self.inclinaison)
        return nouvelle_orbite

    def desorbitation(self, satellite, orbite, position, atmosphere, plot_orbit=False, force_propulsion=0):
        # Calcul et affichage de la trajectoire du satellite en orbite

        # Initialisation des variables
        temps = []
        altitude = []
        vitesse = []
        acceleration_radiale = []
        acceleration_tangentielle = []
        acceleration = []

        # Conditions de position initiales
        match position:
            case Position_manoeuvre.perigee:
                altitude.append(self.perigee + rayon_terre)
            case Position_manoeuvre.apogee:
                altitude.append(self.perigee + rayon_terre)

        vitesse.append(np.sqrt(mu_terre / altitude[0]))
        temps.append(0)
        # Calcul de la trajectoire avec la méthode d'Euler

        i = 0
        # Tant que le satellite n'atteint pas 100 km
        while altitude[i] > 100000:

            # Force gravitationnelle et de trainee
            force_gravite = -mu_terre / (altitude[i] ** 2)
            import pdb; pdb.set_trace()
            densite_air = atmosphere.densite[int(altitude[i])//1000]
            force_trainee = 0.5 * densite_air * satellite.surface * np.power(vitesse[i], 2) * satellite.cx

            # Calcul des composantes radiales et tangentielle des forces
            force_radiale = force_gravite
            force_tangentielle = force_propulsion + force_trainee

            # Calcul de l'accélération radiale et tangentielle
            acceleration_radiale.append(force_radiale / satellite.mass)
            acceleration_tangentielle.append(force_tangentielle / satellite.mass)

            # Accélération = (somme des forces / masse), ne prends pas en compte la difference
            # de masse au cours de la manoeuvre
            acceleration.append((force_gravite + force_propulsion) / satellite.mass)

            # Mise à jour de la vitesse et de l'altitude
            vitesse.append((vitesse[i] + acceleration_tangentielle[i] * self.dt))
            altitude.append(mu_terre / vitesse[i]**2)
            temps.append(temps[i] + self.dt)
            i += 1



        # Affichage des trajectoires
        jour = []
        for j in range(len(temps)):
            jour.append(temps[j] / (24 * 3600))

        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set_title('Altitude en fonction du temps')
        ax.set_xlabel('Temps [J]')
        ax.set_ylabel('Altitude [m]')
        ax.set_title('Altitude du satellite')
        plt.title('Altitude du satellite')
        plt.plot(jour, altitude)
        plt.show()

        if plot_orbit :
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(altitude * np.cos(temps), altitude * np.sin(temps), np.zeros_like(temps), label='Trajectoire du satellite')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_title('Trajectoire du satellite en orbite')
            plt.legend()
            plt.show()