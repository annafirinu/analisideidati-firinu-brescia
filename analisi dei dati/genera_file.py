import random

def genera_file_txt(nome_file, n=50, min_val=1, max_val=100):
    with open(nome_file, "w") as f:
        for _ in range(n):
            f.write(f"{random.randint(min_val, max_val)}\n")
    print(f"File {nome_file} generato con {n} numeri casuali.")