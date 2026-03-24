import pandas as pd

wage = pd.read_csv('salario.csv')

wage['Salário'] = wage['Salário'].replace(r'[^\d.]', '', regex=True).astype(float)

mediaIdade = wage['Idade'].mean()
mediaSalario = round(wage['Salário'].mean(), 2)


print(f'A média das idades é de: {mediaIdade:.1f} anos.')
print(f'A média salarial é de: R$ {mediaSalario}')