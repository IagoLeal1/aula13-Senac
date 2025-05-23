import pandas as pd

# pip install openpyxl
df = pd.read_excel('./aula_13/vendas_eletronicos.xlsx')
print(df.head())  # imprime as 5 primeiras linhas

print(30*'=')
print('Menor Valor:')
print(df['Faturamento Total (R$)'].min())

print(30*'=')
print('Maior Valor:')
print(df['Faturamento Total (R$)'].max())

print(30*'=')
print('Total de Unidades Vendidas:')
print(df['Unidades Vendidas'].sum())

print(30*'=')
print('Média:')
print(df['Preço por Unidade (R$)'].mean())