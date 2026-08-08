#Remover Duplicatas: Receba uma lista de e-mails de participantes confirmados para um evento (onde alguns e-mails podem estar duplicados). Use um Set (Conjunto) para limpar e obter apenas os participantes únicos.

#Dados Fixos (Tupla): Armazene as informações do evento (Nome do Evento, Data, Limite de Vagas) em uma Tupla, garantindo que esses metadados nunca sejam alterados durante a execução do programa.

#Mapeamento (Dicionário): Crie um dicionário para associar os e-mails únicos dos participantes às suas respectivas áreas de interesse (ex: {"email@teste.com": "Python", "outro@teste.com": "Data Science"}). Use o método .get(email, "Não informado") para buscar o interesse de um participante de forma segura.



if __name__ == "__main__":
    
    evento = ('Evento teste', '07/08/2026', 150)
    
    
    lista_email = {'ale.leleco@gmail.com', "meyre.baqueta@gmail.com", "elisa.silva@gmail.com", "Carlos.maos@gmail.com", "ale.leleco@gmail.com", "joao@gmail.com", "marcelo@g.gmail.com", "elisa"}
    
    lista_unica = list(set(lista_email))
    
    print(lista_unica)
    print(evento)