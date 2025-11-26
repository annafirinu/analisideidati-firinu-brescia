import numpy as np

def genera_csv():
    righe = int(input("Numero di righe: "))
    colonne = int(input("Numero di colonne: "))
    totale = righe * colonne
    dati = np.random.randint(0, 101, size=totale)
    matrice = dati.reshape((righe, colonne))
    nome_file = input("Nome del file CSV da creare: ").strip()
    np.savetxt(nome_file + ".csv", matrice, fmt='%d', delimiter=',')
    print(f"File '{nome_file}.csv' creato con {righe} righe e {colonne} colonne.")
    
    return matrice
        

