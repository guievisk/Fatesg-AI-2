import pandas as pd

faturamento = {'Mes': ['Jan', 'Fev', 'Mar'], 'Lucro': [15000, 18200, 21000]}
df_financeiro = pd.DataFrame(faturamento)

print("--- Transposta ---")
print(df_financeiro.T)
print("\n--- Tipos de Dados ---")
print(df_financeiro.dtypes)
print("\n--- Tamanho Total (Células) ---")
print(df_financeiro.size)
print("\n--- Último Registro ---")
print(df_financeiro.tail(1))