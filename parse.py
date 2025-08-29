#   ___                   _       _        
#  / _ \ _   _  __ _ _ __| |_ ___| |_ ___  
# | | | | | | |/ _` | '__| __/ _ \ __/ _ \ 
# | |_| | |_| | (_| | |  | ||  __/ || (_) |
#  \__\_\\__,_|\__,_|_|   \__\___|\__\___/ 
# Linguagem: Quarteto Language
# Autor: Seu nome
# Versão: 1.0
# Data: 28-08-2025

def interpretador(codigo, variaveis=None):
    # quebra o codigo em linhas
    if variaveis is None:
        #um dicionario para armazenar as variaveis
        variaveis = {}

    def eval_texto(expr):
        partes = [p.strip() for p in expr.split("+")]
        out = ""
        for p in partes:
            if len(p) >= 2 and p[0] == '"':
                out += p[1:-1] #trecho entre as aspas
            else:
                out += str(variaveis.get(p, p)) # variavel (literal se nao existir)
        return out
    linhas = codigo.split('\n')
    for linha in linhas:
        linha = linha.strip() # remove espaços desnecessarios
        if not linha: #ignora linhas vazias
            continue

        #se for uma linha de definir
        if linha.startswith("definir"):
            resto = linha[7:].strip()
            if ' como ' not in resto:
                print(f"Erro de sintaxe: {linha}")
                continue
            nome, valor = resto.split(" como ", 1) 
            nome = nome.strip()
            valor = valor.strip()
            if len(valor) >= 2 and valor[0] == '"' and valor[1] == '"':
                valor = valor [1:-1]
            variaveis[nome] = valor
        
        #se for uma linha de mostrar
        elif linha.startswith("mostrar"):
            conteudo = linha[7:].strip()
            print(eval_texto(conteudo))

        #se for uma estrutura condicional (se)
        elif linha.startswith("se"):
            resto = linha[3:].strip()
            if " então " not in resto:
                print(f"Erro de sintaxe: {linha}")
                continue
            condicao, comando = resto.split(" então ", 1)
            #aqui podemos apenas checar se a condição pé verdadeira ou falsa
            if condicao.strip() == "verdadeiro":
                interpretador(comando.strip(), variaveis) #executa o comando dentro da condição

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



codigo_exemplo = """
    definir nome como "lalala"
    mostrar "O nome é" + nome    
    se verdadeiro então mostrar "Isso é verdadeiro"
    enquanto verdadeiro faça mostrar "Dentro do laço"
"""
escolha = input("Digite 1 para rodar o codigo de exemplo ou 2 para digitar o seu proprio codigo")

if escolha == "1":
    interpretador(codigo_exemplo)
elif escolha == "2":
    print("Digite seu codigo (linha a linha). Para terminar deixe a linha em branco e pressione enter ou digite 'fim'")
    linhas = []
    while True:
        linha = input()
        if not linha or linha.strip().upper() == "FIM":
            break
        linhas.append(linha)
    codigo_usuario = "\n".join(linhas)
    interpretador(codigo_usuario)
else: 
    print("Opção invalida!")
