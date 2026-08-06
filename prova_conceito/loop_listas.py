
if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = []
    for n in numeros:
        mod = n % 2
        if mod == 0:
            pares.append(n)

    print(f"Os números pares da lista são: {pares}")

