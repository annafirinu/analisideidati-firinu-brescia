import numpy as np

# Funzioni di analisi 1D
def analisi_base_1D(arr):
    print("=== Statistiche di base 1D ===")
    print(f"Minimo: {np.min(arr)}")
    print(f"Massimo: {np.max(arr)}")
    print(f"Media: {np.mean(arr)}")
    print(f"Deviazione standard: {np.std(arr)}")

def analisi_posizionale_1D(arr):
    print("=== Analisi posizionale 1D ===")
    print(f"Indice del minimo: {np.argmin(arr)}")
    print(f"Indice del massimo: {np.argmax(arr)}")
    print(f"Mediana: {np.percentile(arr, 50)}")
    x = float(input("Inserisci un valore per searchsorted: "))
    pos = np.searchsorted(np.sort(arr), x)
    print(f"Posizione ordinata di inserimento di {x}: {pos}")

def analisi_aggregazioni_2D(matrix):
    print("=== Aggregazioni per assi ===")
    print(f"Somma per colonne: {np.sum(matrix, axis=0)}")
    print(f"Somma per righe: {np.sum(matrix, axis=1)}")
    print(f"Media colonnare: {np.mean(matrix, axis=0)}")
    print(f"Media per riga: {np.mean(matrix, axis=1)}")

def analisi_matriciale_2D(matrix):
    print("=== Operazioni matriciali ===")
    print(f"Trasposizione:\n{np.transpose(matrix)}")
    print(f"Norma della matrice: {np.linalg.norm(matrix)}")
    if matrix.shape[0] == matrix.shape[1]:
        print(f"Prodotto matriciale con se stessa:\n{np.dot(matrix, matrix)}")
    if matrix.shape[0] > 1:
        print(f"Matrice di covarianza:\n{np.cov(matrix.T)}")

def carica_file(nome_file, delimiter=','):
    arr = np.loadtxt(nome_file, delimiter=delimiter)
    if arr.ndim == 1:
        print("Array 1D caricato.")
    else:
        print("Array multidimensionale caricato.")
    return arr

        
def salva_file(nome_file, data):
    np.savetxt(nome_file, data, delimiter=',', fmt='%g')
    print(f"Dati salvati in {nome_file}")

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Analizza file")
        print("2. Esci")
        scelta = input("Seleziona un'opzione (1/2): ")

        match scelta:
            case '1':
                file_input = input("Inserisci il nome del file (TXT o CSV): ")
                dati = carica_file(file_input)

                if dati.ndim == 1:
                    analisi_base_1D(dati)
                    analisi_posizionale_1D(dati)
                else:
                    analisi_aggregazioni_2D(dati)
                    analisi_matriciale_2D(dati)

                salva = input("Vuoi salvare i dati in un CSV? (s/n): ").lower()
                if salva == 's':
                    nome_output = input("Nome file di output: ")
                    salva_file(nome_output, dati)

            case '2':
                print("Uscita dal programma.")
                break

            case _:
                print("Opzione non valida, riprova.")

if __name__ == "__main__":
    main()
