import pandas as pd

# 1. IMPORTAÇÃO (Passo 5)
# O BDE usa ';' e latin-1. O VS Code mostrou que os anos são colunas.
df = pd.read_csv('consulta.csv', sep=';', encoding='latin-1')

# 2. MANIPULAÇÃO E LIMPEZA (EDA - Passo 6)
# Removendo pontos de milhar (ex: '1.288' -> '1288') e convertendo para número
anos = [str(ano) for ano in range(2014, 2025)]
for ano in anos:
    df[ano] = df[ano].astype(str).str.replace('.', '').astype(int)

# "Derretendo" o dataframe para ficar no formato longo (Melhor para BI)
df_long = df.melt(id_vars=['Localidade', 'Variável'], 
                  value_vars=anos, 
                  var_name='Ano', 
                  value_name='Qtd_Docentes')

print("--- Resumo da Análise Exploratória (EDA) ---")
print(df_long.info())
print(df_long.describe())

# 3. CÁLCULO DE KPIs (Passo 7)
# Vamos separar os dados para calcular
df_pivot = df_long.pivot_table(index=['Localidade', 'Ano'], 
                               columns='Variável', 
                               values='Qtd_Docentes').reset_index()

# Ajustando nomes das colunas para facilitar
df_pivot.columns = ['Cidade', 'Ano', 'Estadual', 'Particular']

# KPI 1: Índice de Participação Privada (IPP) 
# Estratégico para BI: Mostra quanto da educação depende do setor privado
df_pivot['KPI_Participacao_Privada'] = (df_pivot['Particular'] / (df_pivot['Estadual'] + df_pivot['Particular'])) * 100

# KPI 2: Razão de Crescimento (YoY)
# Mostra a expansão da rede ano a ano
df_pivot['KPI_Crescimento_Total'] = df_pivot.groupby('Cidade')['Estadual'].pct_change() * 100

# KPI 3: Índice de Predomínio Público
# Identifica se a cidade tem um perfil mais voltado ao ensino estatal
df_pivot['KPI_Predominio_Publico'] = df_pivot['Estadual'] / df_pivot['Particular']

print("\n--- Resultados dos KPIs de Business Intelligence ---")
print(df_pivot[['Cidade', 'Ano', 'KPI_Participacao_Privada', 'KPI_Crescimento_Total']].head(10))

# Salvando o resultado final para você entregar ou fazer gráficos
df_pivot.to_csv('resultado_kpis_bi.csv', index=False)

import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o estilo do gráfico
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_pivot, x='Ano', y='KPI_Participacao_Privada', hue='Cidade', marker='o')

plt.title('Evolução do Índice de Participação Privada (2014-2024)')
plt.ylabel('Percentual de Docentes (%)')
plt.xlabel('Ano')
plt.grid(True)

# Salva o gráfico como imagem para você colar no Word/Docs
plt.savefig('grafico_bi_docentes.png')
plt.show()