import numpy as np

def stampa_argmin(arr):
    print("Indice del valore minimo (argmin):", np.argmin(arr))

def stampa_argmax(arr):
    print("Indice del valore massimo (argmax):", np.argmax(arr))

def stampa_percentile(arr, p=50):
    print(f"Percentile {p}:", np.percentile(arr, p))

def stampa_searchsorted(arr, x):
    posizione = np.searchsorted(np.sort(arr), x)
    print(f"Posizione ordinata per inserire {x}:", posizione)

