import numpy as np

def pulisci_dati(arr):
    numeri = []

    for x in arr:
        x = x.strip()

        if x.isdigit():      # accetta solo numeri interi POSITIVI
            numeri.append(int(x))

    # trasformo la lista pulita in un array NumPy
    return np.array(numeri)
