import os as np
import random

class Enregistrement:
    def __init__(self, temperature, humidite, precipitations, vent):
        self._temperature = temperature
        self._humidite = humidite
        self._precipitations = precipitations
        self._vent = vent
    def __str__(self):
        return (
            f"Température: {self._temperature}°C, "
            f"Humidité: {self._humidite}%, "
            f"Précipitations: {self._precipitations}mm, "
            f"Vent: {self._vent}km/h"
        )
    def get_temperature(self):
        return self._temperature
    def set_temperature(self, temperature):
        self._temperature = temperature
    def get_humidite(self):
        return self._humidite
    def set_humidite(self, humidite):
        self._humidite = humidite
    def get_precipitations(self):
        return self._precipitations
    def set_precipitations(self, precipitations):
        self._precipitations = precipitations
    def get_vent(self):
        return self._vent
    def set_vent(self, vent):
        self._vent = vent
    def score(self):
        score = 0
        if 18 <= self._temperature <= 28:
            score += 40
        elif 10 <= self._temperature < 18 or 28 < self._temperature <= 32:
            score += 30
        elif self._temperature < 10 or self._temperature > 32:
            score += 10
        if 40 <= self._humidite <= 70:
            score += 20
        elif 30 <= self._humidite < 40 or 70 < self._humidite <= 80:
            score += 10
        elif self._humidite < 30 or self._humidite > 80:
            score += 5
        if 0 <= self._precipitations <= 2:
            score += 20
        elif 2 < self._precipitations <= 10:
            score += 10
        if 0 <= self._vent <= 30:
            score += 20
        elif 30 < self._vent <= 60:
            score += 10
        return score

class Station:
    def __init__(self, nom, localisation):
        self._nom = nom
        self._localisation = localisation
        self._data = {}
        self._mois = [
            ("janvier", 31), ("fevrier", 29), ("mars", 31), ("avril", 30),
            ("mai", 31), ("juin", 30), ("juillet", 31), ("aout", 31),
            ("septembre", 30), ("octobre", 31), ("novembre", 30), ("decembre", 31)
        ]
        self.charger_donnees()

    def __str__(self):
        return f"Station: {self._nom}, Localisation: {self._localisation}"

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_localisation(self):
        return self._localisation

    def set_localisation(self, localisation):
        self._localisation = localisation

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def charger_donnees(self):
        for mois, jours in self._mois:
            self._data[mois] = {}
            for jour in range(1, jours + 1):
                temperature = random.choice([np.nan, random.randint(0, 40)])
                humidite = random.choice([np.nan, random.randint(40, 90)])
                precipitations = random.choice([np.nan, random.randint(0, 20)])
                vent = random.choice([np.nan, random.randint(0, 100)])
                self._data[mois][jour] = Enregistrement(temperature, humidite, precipitations, vent)

    def temperatures_uniques(self, mois):
        return {self._data[mois][jour].get_temperature() for jour in self._data[mois] if not np.isnan(self._data[mois][jour].get_temperature())}

    def temperature_moyenne(self, mois):
        temperatures = [self._data[mois][jour].get_temperature() for jour in self._data[mois] if not np.isnan(self._data[mois][jour].get_temperature())]
        return sum(temperatures) / len(temperatures) if temperatures else np.nan

    def jours_pluvieux(self, mois):
        return [jour for jour in self._data[mois] 
                if not np.isnan(self._data[mois][jour].get_precipitations()) 
                and 
                self._data[mois][jour].get_precipitations() > 0]

    def jours_extrems(self, mois):
        return [jour for jour in self._data[mois] 
                if not np.isnan(self._data[mois][jour].get_temperature()) 
                and 
                (self._data[mois][jour].get_temperature() < 5 or self._data[mois][jour].get_temperature() > 35)]

    def jours_beaux(self, mois):
        return [jour for jour in self._data[mois] if self._data[mois][jour].score() >= 80]

    def score_moyen(self, mois):
        scores = [self._data[mois][jour].score() for jour in self._data[mois]]
        return sum(scores) / len(scores) if scores else np.nan

    def mois_beau(self):
        return max(self._data, key=lambda mois: self.score_moyen(mois), default=None)

station_A = Station("Station A", (1.23, 4.56))
station_B = Station("Station B", (7.89, 10.11))
station_C = Station("Station C", (12.13, 14.15))
station_D = Station("Station D", (16.17, 18.19))

print(station_A)
print("Temperatures uniques en janvier (Station A):", station_A.temperatures_uniques("janvier"))
print("Temperature moyenne en fevrier (Station B):", station_B.temperature_moyenne("fevrier"))
print("Jours pluvieux en mars (Station C):", station_C.jours_pluvieux("mars"))
print("Jours extremes en avril (Station D):", station_D.jours_extrems("avril"))
print("Jours beaux en mai (Station A):", station_A.jours_beaux("mai"))
print("Score moyen en juin (Station B):", station_B.score_moyen("juin"))
print("Mois le plus beau de l'annee (Station C):", station_C.mois_beau())

with open('stations.pkl', 'wb') as fichier:
    pickle.dump([station_A, station_B, station_C, station_D], fichier)

print("Stations sauvegardees dans stations.pkl")
