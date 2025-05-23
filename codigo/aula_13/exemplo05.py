import pandas as pd
import numpy as np

df = pd.read_excel('./aula_13/vendas_roupas.xlsx')
print(df.head())
# print(df.describe())

categoria = df['Categoria']
quantidade_vendida = df['Unidades Vendidas']

media = np.mean(quantidade_vendida)
mediana = np.median(quantidade_vendida)

print(30*'=')
print(media)

print(30*'=')
print(mediana)

# organiizar o DataFrame crescente por 'Quantidade Vendida'
quantidade_vendida = df.sort_values(by='Unidades Vendidas', ascending=True)
# print(quantidade_vendida)

print(30*'=')
print(quantidade_vendida.values)

sastifacao = df[df['Satisfação'] == 'baixo']
print(sastifacao)
