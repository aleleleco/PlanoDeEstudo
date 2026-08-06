def analisar_estoque (dado):
    return min(dado, key=dado.get)
        

if __name__ == "__main__":
    estoque = {
        "caneta": 50,
        "lapis": 100,
        "Sufite" :36,
        "borracha": 300,
        "lapiseira": 150
        
    }

    menor = analisar_estoque(estoque)
    print(f"O item com menor estoque é: {menor} com {estoque[menor]} unidades")