import numpy as np

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

