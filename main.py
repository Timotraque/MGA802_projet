from objet_orbite import *

terre = Planet(6000, 3000)
mars = Planet(2000, 2000, color='r')

space = Two_body_problem(terre, mars, 10000,0)
# space.show()

# Exemple d'utilisation
perigee = 800*10**3  # Altitude du périgée en kilomètres
apogee = 600*10**3  # Altitude de l'apogée en kilomètres
inclinaison = 0  # Inclinaison de l'orbite en degrés

#orbite = Orbite(perigee, apogee, inclinaison)
#orbite.plot_orbit()


# Exemple d'utilisation
perigee = 200 * 10**3   # Altitude du périgée [m]
apogee = 600 * 10**3    # Altitude de l'apogée [m]
inclinaison = 0         # Inclinaison de l'orbite [°]

orbite_initiale = Orbite(perigee, apogee, inclinaison)
#orbite_initiale.plot_orbit()

# ---------------------Manoeuvre---------------------
delta_v = 1000  # Changement de vitesse en m/s
direction = Type_manoeuvre.prograde  # Direction de la manoeuvre ('prograde', 'retrograde' ou 'radiale')
position_perigee = Position_manoeuvre.perigee   # Position de la manoeuvre ('perigee' ou 'apogee'
spoutnik = Satellite(100, 1, 1)
atmosphere_terrestre = Atmosphere()

nouvelle_orbite = orbite_initiale.manoeuvre(delta_v, direction, position_perigee)
#nouvelle_orbite.plot_orbit()

nouvelle_orbite.desorbitation(spoutnik, nouvelle_orbite, position_perigee,atmosphere_terrestre)
