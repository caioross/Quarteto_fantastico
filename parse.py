#   ___                   _       _        
#  / _ \ _   _  __ _ _ __| |_ ___| |_ ___  
# | | | | | | |/ _` | '__| __/ _ \ __/ _ \ 
# | |_| | |_| | (_| | |  | ||  __/ || (_) |
#  \__\_\\__,_|\__,_|_|   \__\___|\__\___/ 
# Linguagem: Quarteto Language
# Autor: Seu nome
# Versão: 1.0
# Data: 28-08-2025

def interpretador(codigo):
    # quebra o codigo em linhas
    linhas = codigo.split('\n')

    #um dicionario para armazenar as variaveis
    variaveis = {}

    for linha in linhas:
        linha = linha.strip() # remove espaços desnecessarios

        #se for uma linha de definir
        if linha.startswith("definir"):
            partes = linha[7:].strip().split(" como ") #pega o nome da variavel e o valor
            nome = partes[0].strip()
            valor = partes[1].strip().strip('"') #remove as aspas
            variaveis[nome] = valor #armazenando a variavel 

        #se for uma linha de mostrar
        elif linha.startswith("mostrar"):
            conteudo = linha[7:].strip().strip('"')
            print(conteudo)

        #se for uma estrutura condicional (se)
        elif linha.startswith("se"):
            condicao = linha[3:].split(" então ")[0].strip()
            comando = linha.split(" então ")[1].strip()

            #aqui podemos apenas checar se a condição pé verdadeira ou falsa
            if condicao == "verdadeiro":
                interpretador(comando) #executa o comando dentro da condição

        #se for um laço "enquanto"
        elif linha.startswith("enquanto"):
            condicao = linha[8:].split(" faça ")[0].strip()
            comando = linha.split(" faça ")[1].strip()

            #verifica a condição do looping (por enquanto , consideramos verdadeiro ou falso)
            while condicao == 'verdadeiro':
                interpretador(comando) # executa o comando dentro do loop
                break # evita loops infinitos para esse exemplo
        else:
            print(f'Comando não foi reconhecido{linha}')
codigo = """
    definir nome como "lalala"
    mostrar "O nome é" + nome    
    se verdadeiro então mostrar "Isso é verdadeiro"
    enquanto verdadeiro faça mostrar "Dentro do laço"
"""
interpretador(codigo)