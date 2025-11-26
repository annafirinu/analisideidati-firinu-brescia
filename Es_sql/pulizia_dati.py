import numpy as np

def pulisci_dati_2D(arr_2d):

    matrice_pulita = []

    # determina numero massimo di colonne
    max_col = max(len(riga) for riga in arr_2d)

    for riga in arr_2d:
        riga_pulita = []
        for x in riga:
            x = str(x).strip()
            if x.replace(".", "", 1).replace("-", "", 1).isdigit():
                riga_pulita.append(float(x))
            else:
                riga_pulita.append(np.nan)  # valori mancanti diventano NaN
        # completa la riga se troppo corta
        while len(riga_pulita) < max_col:
            riga_pulita.append(np.nan)
        matrice_pulita.append(riga_pulita)

    return np.array(matrice_pulita, dtype=float)