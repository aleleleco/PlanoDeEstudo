
def verifica_temperatura(temperatura):
   if temperatura < 15:
         print("Frio!")
   elif  temperatura >= 15 and temperatura <= 25:
            print("Agradável!")
   else:
            print("Está quente!")

if __name__ == "__main__":
    temperatura = float(input("Qual a temperatura atual? "))

    verifica_temperatura(temperatura)


    