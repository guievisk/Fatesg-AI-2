import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# 1. Configuração inicial do Dashboard
# ----------------------------------------------------
st.set_page_config(layout="wide")
st.title('Dashboard Financeiro - Agro Goiás - 2014-2024')
st.write('### Inteligência de Negócios (Business Intelligence - BI)')

# ----------------------------------------------------
# 2. Carregamento e Tratamento de Dados
# ----------------------------------------------------
# Carregando o arquivo
df = pd.read_csv("financiamentoPecuaria.csv", encoding='utf-8-sig', sep=';')

# Removendo a coluna 'Variável' caso exista
if 'Variável' in df.columns:
    df = df.drop(columns=['Variável'])

# Colunas que contêm os anos (da segunda coluna em diante)
colunas_anos = df.columns[1:]

# Convertendo cada coluna de ano para número (Float) de forma segura
for col in colunas_anos:
    texto = df[col].astype(str).str.strip()
    texto = texto.replace('-', '0') 
    texto = texto.str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    df[col] = pd.to_numeric(texto, errors='coerce').fillna(0).round(2)

# Criando uma coluna com a média de investimentos para cada localidade
df["Md_Invest"] = df[colunas_anos].mean(axis=1).round(2)

# Inserir uma linha com a média de investimento para cada ano
mean_values = df[colunas_anos].mean().round(2)
nova_linha = ["Média"] + mean_values.tolist() + [mean_values.mean().round(2)]

# Concatena a nova linha ao dataframe original
df_media = pd.DataFrame([nova_linha], columns=df.columns)
df = pd.concat([df, df_media], ignore_index=True)

# ----------------------------------------------------
# 3. Estrutura da Barra Lateral (Sidebar)
# ----------------------------------------------------
df["Localidade"] = df["Localidade"].astype(str).str.strip()

localidades = df.loc[df["Localidade"] != "Média", "Localidade"].unique().tolist()
opcoes_localidade = ["Todos"] + localidades
localidade_selecionada = st.sidebar.selectbox("Selecione a Localidade:", opcoes_localidade)

# Filtra o dataset de acordo com a seleção
if localidade_selecionada != "Todos":
    df_local = df[df["Localidade"] == localidade_selecionada]
else:
    df_local = pd.DataFrame()

# ----------------------------------------------------
# 4. Construção dos Gráficos (Colunas)
# ----------------------------------------------------
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    if localidade_selecionada == "Todos":
        df_plot = df[df["Localidade"] != "Média"]
        investimentos_ano = df_plot[colunas_anos].mean()
        st.write("### Média dos investimentos por ano (Todas as localidades)")
        st.bar_chart(investimentos_ano)
    else:
        st.write(f"### Dados filtrados para {localidade_selecionada}:")
        st.dataframe(df_local)
        
        if not df_local.empty:
            investimentos_local = df_local.iloc[0][colunas_anos]
            st.write(f"### Evolução dos investimentos para {localidade_selecionada}:")
            st.bar_chart(investimentos_local)
        else:
            st.error("Nenhum dado encontrado para essa localidade.")

with col2:
    st.write("### Gráfico de Linhas: Evolução dos Investimentos")
    if localidade_selecionada == "Todos":
        investimentos_ano = df[df["Localidade"] != "Média"][colunas_anos].mean()
    else:
        if not df_local.empty:
            investimentos_ano = df_local.iloc[0][colunas_anos]
        else:
            investimentos_ano = []
            
    st.line_chart(investimentos_ano)

with col3:
    st.write("### Comparação da Cidade com a Média Geral")
    if localidade_selecionada != "Todos" and not df_local.empty:
        investimentos_local = df_local.iloc[0][colunas_anos]
        investimentos_media = df[df["Localidade"] != "Média"][colunas_anos].mean()
        
        df_comparacao = pd.DataFrame({
            "Ano": colunas_anos,
            localidade_selecionada: investimentos_local.values,
            "Média Geral": investimentos_media.values
        })
        df_comparacao.set_index("Ano", inplace=True)
        st.bar_chart(df_comparacao)
    else:
        st.info("Selecione uma localidade para visualizar a comparação.")

with col4:
    if localidade_selecionada != "Todos" and not df_local.empty:
        st.write("### Ano com Maior Investimento")
        investimentos_local = df_local.iloc[0][colunas_anos]
        
        ano_max = investimentos_local.idxmax()
        valor_max = investimentos_local.max()
        
        st.metric(label="Ano com Maior Investimento", value=ano_max, delta=f"Valor: R$ {valor_max:,.2f}")
    else:
        st.info("Selecione uma localidade específica para visualizar o ano com maior investimento.")