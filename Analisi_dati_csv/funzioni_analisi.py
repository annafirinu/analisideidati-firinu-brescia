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
