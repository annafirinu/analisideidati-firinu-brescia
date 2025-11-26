from genera_file import *
from statistiche_base import stampa_min, stampa_max, stampa_media, stampa_dev_std
from analisi_posizionale import stampa_argmin, stampa_argmax, stampa_percentile, stampa_searchsorted
from pulizia_dati import *
from creazione_file import genera_csv
from funzioni_analisi import *


# Carica file TXT come lista di stringhe
def carica_file(file_path):
    arr = []
    with open(file_path, "r") as f:
        for line in f:
            arr.append(line.strip())
    return arr


def main():
    file_path = "dati.txt"

    # Genera file txt con numeri casuali
    genera_file_txt(file_path, n=50)
    
    #Genera csv e crea matrice
    matrix = genera_csv()

    # Carica come lista grezza
    arr_grezzo = carica_file(file_path)

    # Pulisci i dati e crea array numpy
    arr = pulisci_dati(arr_grezzo)
    

    print("Array numerico pulito creato correttamente.")

    while True:
        print("\nMenu Analisi")
        print("1. Valore minimo")
        print("2. Valore massimo")
        print("3. Media")
        print("4. Deviazione standard")
        print("5. Indice valore minimo (argmin)")
        print("6. Indice valore massimo (argmax)")
        print("7. Percentile")
        print("8. Searchsorted")
        print("9. Esegui tutte le statistiche di base")
        print("10. Esegui tutte le analisi posizionali")
        print("11. Esegui tutte le analisi aggregazioni 2D")
        print("12. Esegui tutte le analisi matriciali 2D")
        print("13. Esegui tutte le analisi 1D")
        print("14. Mostra array iniziale")
        print("15. Mostra matrice iniziale")
        print("0. Esci")

        scelta = input("Inserisci scelta: ")

        if scelta == "1":
            stampa_min(arr)
        elif scelta == "2":
            stampa_max(arr)
        elif scelta == "3":
            stampa_media(arr)
        elif scelta == "4":
            stampa_dev_std(arr)
        elif scelta == "5":
            stampa_argmin(arr)
        elif scelta == "6":
            stampa_argmax(arr)
        elif scelta == "7":
            p = float(input("Inserisci percentile (0-100): "))
            stampa_percentile(arr, p)
        elif scelta == "8":
            x = float(input("Valore da inserire per searchsorted: "))
            stampa_searchsorted(arr, x)
        elif scelta == "9":
            stampa_min(arr)
            stampa_max(arr)
            stampa_media(arr)
            stampa_dev_std(arr)
        elif scelta == "10":
            stampa_argmin(arr)
            stampa_argmax(arr)
            for p in [25, 50, 75]:
                stampa_percentile(arr, p)
            for x in [30, 50, 70]:
                stampa_searchsorted(arr, x)
                
        elif scelta == "11":
            analisi_aggregazioni_2D(matrix)
            
        elif scelta == "12":
            analisi_matriciale_2D(matrix)
            
        elif scelta == "13":
            stampa_min(arr)
            stampa_max(arr)
            stampa_media(arr)
            stampa_dev_std(arr)
            stampa_argmin(arr)
            stampa_argmax(arr)
            for p in [25, 50, 75]:
                stampa_percentile(arr, p)
            for x in [30, 50, 70]:
                stampa_searchsorted(arr, x)
                
        elif scelta == "14":
            print("\nArray iniziale:")
            print(arr)
            
        elif scelta == "15":
            print("\nMatrice iniziale:")
            print(matrix)
            
        elif scelta == "0":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    main()


