import pandas as pd 
wage = pd.read_csv('salario.csv')

wage = wage.rename(columns={'Nome':'Colaborador(a)'}).head()
print(wage)