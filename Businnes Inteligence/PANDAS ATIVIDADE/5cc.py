import pandas as pd 
wage = pd.read_csv('salario.csv')

mais_velho = wage.loc[wage['Idade'] == wage['Idade'].max()]
print(mais_velho)