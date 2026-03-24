import pandas as pd 
wage = pd.read_csv('salario.csv')

mais_novo = wage.loc[wage['Idade'] == wage['Idade'].min()]
print(mais_novo)