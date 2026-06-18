import requests
import json

# 1. Suas Credenciais de Acesso
ID_DO_BANCO = "e34aa922-5bfd-4e82-a9c6-ed0494ef9f99"
REGIAO_AWS = "us-east-2"
MEU_TOKEN_ASTRA = "token api da cassandra" 

def consultar_leituras_cassandra():
    api_url = f"https://{ID_DO_BANCO}-{REGIAO_AWS}.apps.astra.datastax.com/api/rest/v2/keyspaces/default_keyspace/leituras_sensor"

    cabecalhos_requisicao = {
        "X-Cassandra-Token": MEU_TOKEN_ASTRA,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    filtros_busca = {
        "sensor_id": {"$eq": "sensor-001"},
        "data_leitura": {"$eq": "2026-05-22"}
    }
    
    parametros = {
        "where": json.dumps(filtros_busca)
    }

    print("Conectando ao banco Cassandra...")
    
    try:
        resposta = requests.get(api_url, headers=cabecalhos_requisicao, params=parametros)
        
        resposta.raise_for_status() 
        
        dados_retornados = resposta.json()
        print("\n--- Consulta realizada com sucesso! ---")
        
        print(json.dumps(dados_retornados, indent=4, ensure_ascii=False))

    except requests.exceptions.RequestException as erro:
        print(f"\n[ERRO] Falha ao comunicar com a API: {erro}")
        if resposta.text:
            print(f"Detalhes do erro: {resposta.text}")

if __name__ == "__main__":
    consultar_leituras_cassandra()