import csv
import numpy as np
import sqlite3

# ------------------------------
# Percorso al CSV e al DB
# ------------------------------
CSV_PATH = "california_housing_data.csv"
DB_NAME = "analisi_california_housing.db"

# ------------------------------
# Funzione: legge il CSV e pulisce i dati
# ------------------------------
def leggi_colonne(file_path):
    """
    Legge il CSV e restituisce:
    - header: lista dei nomi delle colonne
    - colonne: lista di liste, ogni lista contiene i valori numerici di una colonna
    """
    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # salta intestazione
        n_col = len(header)
        colonne = [[] for _ in range(n_col)]  # crea una lista vuota per ogni colonna

        for riga in reader:
            for i in range(n_col):
                val = riga[i].strip()  # rimuove spazi
                try:
                    val = float(val)     # converte in float
                except:
                    val = np.nan         # valori non numerici diventano NaN
                colonne[i].append(val)

    return header, colonne

# ------------------------------
# Funzione: salva dataset e statistiche nel DB SQLite
# ------------------------------
def salva_dataset_e_statistiche(header, colonne):
    """
    Crea due tabelle nel DB:
    1. california_pulito -> dataset pulito
    2. california_statistiche -> min, max, media, mediana, deviazione standard per ogni colonna
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # -------- Tabella dataset pulito --------
    # Creiamo la definizione delle colonne
    colonne_def = ", ".join([f"{col} REAL" for col in header])

    # Rimuove la tabella precedente se esiste
    cursor.execute("DROP TABLE IF EXISTS california_pulito")

    # Crea tabella nuova
    cursor.execute(f"CREATE TABLE california_pulito ({colonne_def})")

    # Trasposta: da colonne -> righe
    righe = list(zip(*colonne))

    # Inserisce tutte le righe nella tabella
    cursor.executemany(
        f"INSERT INTO california_pulito ({', '.join(header)}) VALUES ({', '.join(['?']*len(header))})",
        righe
    )

    # -------- Tabella statistiche --------
    cursor.execute("DROP TABLE IF EXISTS california_statistiche")
    cursor.execute("""
        CREATE TABLE california_statistiche (
            feature TEXT,
            min REAL,
            max REAL,
            media REAL,
            mediana REAL,
            dev_std REAL
        )
    """)

    # Calcola statistiche per ogni colonna e le inserisce
    for i, col in enumerate(colonne):
        col_array = np.array(col, dtype=float)
        min_val = np.nanmin(col_array)
        max_val = np.nanmax(col_array)
        mean_val = np.nanmean(col_array)
        median_val = np.nanmedian(col_array)
        std_val = np.nanstd(col_array)

        cursor.execute(
            "INSERT INTO california_statistiche (feature, min, max, media, mediana, dev_std) VALUES (?, ?, ?, ?, ?, ?)",
            (header[i], min_val, max_val, mean_val, median_val, std_val)
        )

    # Salva e chiude il DB
    conn.commit()
    conn.close()
    print("Dataset e statistiche salvati correttamente nel DB SQLite.")

# ------------------------------
# Uso
# ------------------------------
header, colonne = leggi_colonne(CSV_PATH)         # legge e pulisce il CSV
salva_dataset_e_statistiche(header, colonne)      # salva dataset e statistiche nel DB
