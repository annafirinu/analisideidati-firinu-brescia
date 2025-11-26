import numpy as np

def pulisci_dati(arr):
    # Trasforma in array NumPy di stringhe
    arr = np.array(arr, dtype=str)
    
    # Rimuove spazi bianchi
    arr = np.char.strip(arr)
    
    
    def is_float(s):
        s = s.replace(".", "", 1)  # rimuove primo punto decimale
        s = s.replace("-", "", 1)  # rimuove segno meno
        return s.isdigit()
    
    # Applica la funzione a tutti gli elementi
    mask = np.vectorize(is_float)(arr)
    
    # Seleziona solo numeri validi e converte in float
    numeri = arr[mask].astype(float)
    
    return numeri

