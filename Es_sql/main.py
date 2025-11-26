from statistiche_base import stampa_min, stampa_max, stampa_media, stampa_dev_std
from analisi_posizionale import stampa_argmin, stampa_argmax, stampa_percentile, stampa_searchsorted
from pulizia_dati import *
import numpy as np
import sqlite3

#1. Caricare il CSV direttamente in NumPy
data = np.genfromtxt("california_housing_data.csv", delimiter=",", skip_header=1)
#Ogni colonna diventa un array NumPy
MedInc      = data[:, 0]
HouseAge    = data[:, 1]
AveRooms    = data[:, 2]
AveBedrms   = data[:, 3]
Population  = data[:, 4]
AveOccup    = data[:, 5]
Latitude    = data[:, 6]
Longitude   = data[:, 7]
MedHouseVal = data[:, 8]

#2. Connessione al database SQLite
conn = sqlite3.connect("housing.db")
cursor = conn.cursor()

#3. Creazione tabella
cursor.execute("""
CREATE TABLE IF NOT EXISTS Housing (
    MedInc REAL,
    HouseAge REAL,
    AveRooms REAL,
    AveBedrms REAL,
    Population REAL,
    AveOccup REAL,
    Latitude REAL,
    Longitude REAL,
    MedHouseVal REAL
);
""")

#4. Inserimento dati usando NumPy
for i in range(data.shape[0]):
    cursor.execute("""
        INSERT INTO Housing VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(data[i]))

conn.commit()
conn.close()

print("Dati caricati da CSV, Creato array per colonna con NumPy, Passati a SQLite") 
