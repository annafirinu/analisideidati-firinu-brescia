import numpy as np

def genera_csv():
    print("Creazione file CSV personalizzato.")
    tipo = input("Vuoi un array 1D o 2D? (1D/2D): ").strip().upper()
    
    if tipo == '1D':
        n = int(input("Quanti numeri vuoi generare? "))
        dati = np.random.randint(0, 101, size=n)
        nome_file = input("Nome del file CSV da creare: ").strip()
        # Scrive tutti i numeri su una riga separati da virgole
        with open(nome_file + ".csv", "w") as f:
            f.write(','.join(map(str, dati)))
        print(f"File '{nome_file}.csv' creato con {n} numeri su una riga.")
        
    elif tipo == '2D':
        righe = int(input("Numero di righe: "))
        colonne = int(input("Numero di colonne: "))
        totale = righe * colonne
        dati = np.random.randint(0, 101, size=totale)
        matrice = dati.reshape((righe, colonne))
        nome_file = input("Nome del file CSV da creare: ").strip()
        np.savetxt(nome_file + ".csv", matrice, fmt='%d', delimiter=',')
        print(f"File '{nome_file}.csv' creato con {righe} righe e {colonne} colonne.")
        
    else:
        print("Tipo non valido. Scrivi '1D' o '2D'.")

genera_csv()
