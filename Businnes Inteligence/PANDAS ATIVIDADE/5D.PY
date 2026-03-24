import pandas as pd 
wage = pd.read_csv('salario.csv')

maior_salario = wage.loc[wage['Salário'] == wage['Salário'].max()]
print(maior_salario)
