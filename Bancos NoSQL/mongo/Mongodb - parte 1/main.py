import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Senai_IA"]
colecao = db["Laptops"]


df = pd.DataFrame(list(colecao.find()))


if 'Price' in df.columns:
    df['Price'] = df['Price'].replace(r'[^\d.]', '', regex=True).astype(float)


print("--- Amostra de 5 Laptops do MongoDB ---")
print(df.head(5))