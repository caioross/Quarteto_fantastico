import requests
from bs4 import BeautifulSoup 
import pandas as pd
import time
import random
import sqlite3
import datetime
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36' 
}
baseURL = "https://www.sampaingressos.com.br/templates/ajax/lista_espetaculo.php"
filmes = []  
data_hoje = datetime.date.today().strftime("%d-%m-%Y")
agora = datetime.datetime.now()
paginaLimite = 1
card_temp_min = 1
card_temp_max = 1
pag_temp_min = 1
pag_temp_max = 1
bancoDados = "C:/Users/integral/Desktop/Python 2 Caio/banco_filmes.db"
saidaCSV = f"C:/Users/integral/Desktop/Python 2 Caio/shows_sampaingressos_{data_hoje}.csv"

for pagina in range(1, paginaLimite + 1):
    url = f"{baseURL}?pagina={pagina}&tipoEspetaculo=shows"
    print(f"Coletando dados da pagina {pagina} : {url}")
    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.text, "html.parser")

    if resposta.status_code != 200:
        print(f"Erro ao carregar a pagina {pagina}. Código do erro é: {resposta.status_code}")
        continue

    cards = soup.find_all("div", id="box_espetaculo")
    for card in cards:
        try:
            titulo_tag = card.find("b", class_="titulo")
            local_tag = card.find("span", class_="local")
            horario_tag = card.find("span", class_="horario")

            titulo = titulo_tag.text.strip() if titulo_tag else "N/A"
            local = local_tag.text.strip() if local_tag else "N/A"
            horario = horario_tag.text.strip() if horario_tag else "N/A"

            if titulo != "N/A":
                filmes.append({
                    "Titulo": titulo,
                    "Local": local,
                    "Horario": horario
                })
            else:
                print("Card sem título (ignorado)")

            tempo = random.uniform(card_temp_min, card_temp_max)
            time.sleep(tempo)
        except Exception as e:
            print(f"Erro ao processar card. Erro: {e}")

    tempo = random.uniform(pag_temp_min, pag_temp_max)
    time.sleep(tempo)

df = pd.DataFrame(filmes)
print(df.head())

df.to_csv(saidaCSV, index=False, encoding="utf-8-sig", quotechar="'", quoting=1)

conn = sqlite3.connect(bancoDados)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shows(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Titulo TEXT,
        Local TEXT,
        Horario TEXT
    )
''')

for evento in filmes:
    try:
        cursor.execute('''
            INSERT INTO shows (Titulo, Local, Horario) VALUES (?,?,?)
        ''', (
            evento['Titulo'],
            evento['Local'],
            evento['Horario']
        ))
    except Exception as e:
        print(f"Erro ao inserir evento {evento['Titulo']} no banco de dados. Código de identificação do erro: {e}.")

conn.commit()
conn.close()

print("---------------------------------------")
print('Dados raspados e salvos com sucesso!')
print(f"\n Arquivo salvo em: {saidaCSV} \n")
print("Obrigado por usar o Sistema de Bot do Seu nome")
print(f"Finalizado em: {agora.strftime('%H:%M:%S')}")
print("---------------------------------------")
