'''
Autor: Seu nome
Data: 27-08-25
Version: 1.0
'''

#caminho do banco de dados
DB_PATH = 'bandodedadosAIS.db'
FLASK_DEBUG = True
FLASK_HOST = '127.0.0.1'
FLASK_PORT = 5000

ROTAS = [
    '/',                        # rota 00
    '/upload',                  # rota 01
    '/consultar',               # rota 02
    '/graficos',                # rota 03  
    '/editar_inadimplencia',    # rota 04
    '/correlacao',              # rota 05
    '/grafico3d',               # rota 06
    '/editar_selic'             # rota 07
    ]