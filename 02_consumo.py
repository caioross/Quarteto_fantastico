from flask import Flask, request, render_template
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.io as pio
import random

#configura o plotly para abrir os arquivos no navegador por padrão
pio.renderers.default = "browser"

#carregar o arquivo drinks.csv
dfDrinks = pd.read_csv(r"C:\Users\integral\Desktop\Python 2 Caio\drinks.csv")
dfAvengers = pd.read_csv(r"C:\Users\integral\Desktop\Python 2 Caio\avengers.csv", encoding='latin1')
#outros encodings de exemplo: uft-16 , cp1252, iso8859-1

#criar o banco de dados em sql e popular com os dados do csv
conn = sqlite3.connect(r"C:\Users\integral\Desktop\Python 2 Caio\bancodados.db")

#inserir as duas novas tabelas no banco de dados
dfDrinks.to_sql("bebidas", conn, if_exists="replace", index=False)
dfAvengers.to_sql("vingadores", conn, if_exists="replace", index=False)
conn.commit()
conn.close()

#iniciar o flask
app = Flask(__name__)

#iniciar o servidor 
if __name__ == '__main__':
    app.run(debug=True)
