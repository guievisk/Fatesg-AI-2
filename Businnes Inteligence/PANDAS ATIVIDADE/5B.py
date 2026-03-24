#5b
import pandas as pd 
wage = pd.read_csv('salario.csv')
print(wage.loc[:, ['Nome']])


