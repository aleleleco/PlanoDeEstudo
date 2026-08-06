def calcular_media(lista_notas, bonus=0.0):
    #Ela deve calcular a média aritmética simples das notas contidas na lista e somar o valor do bonus à média final. O resultado final da média não pode ultrapassar o limite máximo de 10.0.
    total_notas =0
    qtd_notas   =0
    nota_final  =0
    for nota in lista_notas:
        total_notas += nota
        qtd_notas += 1
    
    nota_final = (total_notas/qtd_notas)+bonus
    
    if nota_final >= 10:
        nota_final = 10
    
    return nota_final
    

if __name__ == "__main__":
    
    lista_notas = []
    nota = 0.0
    while nota != "sair":
            nota = input("entre com a nota no formato 0.0 ou digite sair")
            if nota == "sair":
                break
            else:
                try:
                    lista_notas.append(float(nota))
                except:
                    print("Valor Invalido")
         
    media = calcular_media(lista_notas, 0.5)
    
    print(f'Notas digitadas {lista_notas}, média Calculada: {media}')
            
        