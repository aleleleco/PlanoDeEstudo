class Retangulo:
    altura = 0
    largura = 0

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura


if __name__ == "__main__":
    novo_retangulo = Retangulo(10, 5)
    area = novo_retangulo.calcular_area()
    print(f"A área do retângulo é: {area}")