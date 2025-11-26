from statistiche_base import stampa_min, stampa_max, stampa_media, stampa_dev_std
from analisi_posizionale import stampa_percentile
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


 #Statistiche e creazione database statistiche
# Lista dei nomi delle colonne corrispondenti agli array
col_names = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", 
             "Population", "AveOccup", "Latitude", "Longitude", "MedHouseVal"]

# Array già creati in precedenza dal CSV
arrays = [MedInc, HouseAge, AveRooms, AveBedrms, 
          Population, AveOccup, Latitude, Longitude, MedHouseVal]


# Creiamo una lista vuota per contenere tutte le statistiche
statistiche = []

# Ciclo su ciascuna colonna (nome + array corrispondente)
for nome, arr in zip(col_names, arrays):
    # Calcolo valore minimo della colonna
    min_val = stampa_min(arr)
    # Calcolo valore massimo della colonna
    max_val = stampa_max(arr)
    # Calcolo della media aritmetica
    mean_val = stampa_media(arr)
    # Calcolo della deviazione standard
    std_val = stampa_dev_std(arr)
    # Calcolo della mediana (percentile 50)
    median = stampa_percentile(arr, 50)

    # Creiamo una tupla con tutte le informazioni per questa colonna
    statistiche.append((nome, min_val, max_val, mean_val, std_val, median))

# Creiamo (o apriamo) il database SQLite "housing_stats.db"
conn = sqlite3.connect("housing_stats.db")
cursor = conn.cursor()  # Creiamo un cursore per eseguire comandi SQL


# Se esiste una tabella precedente con lo stesso nome, la eliminiamo
cursor.execute("DROP TABLE IF EXISTS HousingStats")

# Creiamo la nuova tabella con 6 colonne:
cursor.execute("""
CREATE TABLE IF NOT EXISTS HousingStats (
    ColumnName TEXT,
    Min REAL,
    Max REAL,
    Mean REAL,
    Std REAL,
    Median REAL
);
""")


# Inseriamo tutte le tuple calcolate in una sola volta usando executemany()
cursor.executemany("""
    INSERT INTO HousingStats VALUES (?, ?, ?, ?, ?, ?)
""", statistiche)

# Salviamo le modifiche nel database
conn.commit()
# Chiudiamo la connessione
conn.close()

print("Statistiche calcolate dagli array e salvate su 'housing_stats.db'")
