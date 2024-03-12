import pandas as pd
import numpy as np

class Atmosphere:
    def __init__(self):
        self.temperature = self.calculer_temperature()
        self.densite = self.calculer_densites()

    def calculer_densite_air(self, altitude):

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

        fichier_f10_7 = pd.read_excel('data/flux_solaire_data.xlsx')
        f_10_7 = float(fichier_f10_7[(fichier_f10_7['Année'] == annee) & (fichier_f10_7['Mois'] == mois)]['Flux ajusté'])   # [W.m-2.Hz-1]

        fichier_Ap = pd.read_excel('data/geomagnetic_data_gfz.xlsx')
        Ap = float(fichier_Ap[(fichier_Ap['year'] == annee) & (fichier_Ap['month'] == mois) & (fichier_Ap['day']==jour) & (fichier_Ap['hour_h']==heure)]['ap'])

        T = 900 + 2.5 * (f_10_7 - 70) + 1.5 * Ap    # [K]

        return T