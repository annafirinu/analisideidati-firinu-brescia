import random

def genera_file_txt(nome_file, n=50):
    stringhe = ["ciao", "test", "abc", "xyz", "hello", "???", "none", "data"]
    simboli = ["@", "#", "!!", "$$", "--", "###"]

    with open(nome_file, "w") as f:
        for _ in range(n):

            scelta = random.choice(["int", "float", "stringa", "simbolo"])

            if scelta == "int":
                f.write(str(random.randint(1, 100)) + "\n")

            elif scelta == "float":
                f.write(str(round(random.uniform(1, 100), 2)) + "\n")

            elif scelta == "stringa":
                f.write(random.choice(stringhe) + "\n")

            elif scelta == "simbolo":
                f.write(random.choice(simboli) + "\n")

    print(f"File {nome_file}")
