import requests
import pymongo
import random

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["startup"]
collection = db["funcionarios"]

url = "https://randomuser.me/api/?results=10&nat=br"

response = requests.get(url).json()
funcionarios = []

for user in response["results"]:
    idade = user['dob']['age']
    
    cargo = "Desenvolvedor" if idade < 30 else "Gerente"
    setor = random.choice(["TI", "RH", "Vendas", "Marketing"])
    salario = random.randint(4000, 12000)

    funcionarios.append({
        "nome": f"{user['name']['first']} {user['name']['last']}",
        "idade": idade,
        "email": user['email'],
        "telefone": user['phone'],
        "cargo": cargo,
        "salario": salario,
        "setor": setor
    })  

# Inserir no banco
collection.insert_many(funcionarios)
print(f"Sucesso! {len(funcionarios)} funcionários inseridos.")