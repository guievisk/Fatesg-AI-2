import redis
import base64
import os

try:
    cliente = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
    cliente.ping()
    print(" Conectado ao Redis com sucesso!")
except Exception as e:
    print(f" Erro de conexão: {e}")
    print("Dica: Verifique se o container no Docker Desktop está rodando com a porta 6379 aberta.")

def converter_e_salvar(caminho_da_imagem, chave_no_banco):
    if not os.path.exists(caminho_da_imagem):
        print(f" Erro: O arquivo '{caminho_da_imagem}' não foi encontrado na pasta!")
        return

    with open(caminho_da_imagem, "rb") as arquivo_imagem:
        conteudo_base64 = base64.b64encode(arquivo_imagem.read()).decode('utf-8')
        cliente.set(chave_no_banco, conteudo_base64)
        print(f" Imagem enviada para o Redis! Chave: {chave_no_banco}")

def recuperar_e_criar_arquivo(chave_no_banco, nome_do_novo_arquivo):
    texto_recuperado = cliente.get(chave_no_banco)
    
    if texto_recuperado:
        dados_binarios = base64.b64decode(texto_recuperado)
        with open(nome_do_novo_arquivo, "wb") as novo_arquivo:
            novo_arquivo.write(dados_binarios)
        print(f" Imagem recuperada do Redis! Arquivo criado: {nome_do_novo_arquivo}")
    else:
        print(" Erro: Não foi possível recuperar os dados do banco.")

if __name__ == "__main__":
    minha_foto = "meu_teste.png" 

    print("--- Iniciando Processo ---")
    converter_e_salvar(minha_foto, "chave_da_minha_foto")
    recuperar_e_criar_arquivo("chave_da_minha_foto", "foto_recuperada.png")
    print("--- Processo Finalizado ---")