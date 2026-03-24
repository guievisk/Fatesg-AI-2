import requests
import psycopg2

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
response = requests.get(url)
dados = response.json()

try:
    conn = psycopg2.connect(
        host="localhost",
        database="atividade_web",
        user="postgres",
        password="Aluno",
        port="5433"
    )
    cur = conn.cursor()

    for moeda in dados:
        preco = dados[moeda]['usd']
        cur.execute(
            "INSERT INTO consulta_moedas (moeda, preco_usd) VALUES (%s, %s)",
            (moeda.capitalize(), preco)
        )

    conn.commit()
    print("Sucesso! Dados armazenados.")
    cur.close()
    conn.close()

except Exception:
    print("Erro: A senha 'admin' ou a porta '5433' estao incorretas.")
    print("Tente mudar a senha para '123456' ou verifique a porta no pgAdmin.")