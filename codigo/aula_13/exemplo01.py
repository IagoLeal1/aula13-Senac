# pip install pandas
import pandas as pd

data = {
    'Nome': ['Ana', 'João', 'Maria'],
    'Idade': [23, 25, 29],
    'Gênero': ['F', 'M', 'F'],
    'Altura': [1.70, 1.80, 1.75],
}

df_dados = pd.DataFrame(data)

print(df_dados)

print('\nVariaveis Quantitativas:')

# idade
print('exibindo a coluna idade')
print(df_dados['Idade'])

# idade
print('exibindo a coluna altura')
print(df_dados['Altura'])