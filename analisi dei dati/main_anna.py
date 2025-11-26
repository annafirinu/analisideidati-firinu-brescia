from genera_file import genera_file_txt
from statistiche_base import stampa_min, stampa_max, stampa_media, stampa_dev_std
from analisi_posizionale import stampa_argmin, stampa_argmax, stampa_percentile, stampa_searchsorted
from pulizia_dati import pulisci_dati


# Carica file TXT come lista di stringhe
def carica_file(file_path):
    arr = []
    with open(file_path, "r") as f:
        for line in f:
            arr.append(line.strip())
    return arr


def main():
    file_path = "dati.txt"

    # Genera file con numeri casuali
    genera_file_txt(file_path, n=50)

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
        print("11. Esegui tutto")
        print("12. Mostra array numerico pulito")
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
        elif scelta == "12":
            print("\nArray NumPy pulito:")
            print(arr)
        elif scelta == "0":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    main()


