import numpy as np
import pandas as pd

df = pd.read_excel('./aula_13/vendas_eletos_eletronicos2.xlsx')

q1 = np.quantile(df['Unidades Vendidas'], 0.25)
q2 = np.quantile(df['Unidades Vendidas'], 0.50)
q3 = np.quantile(df['Unidades Vendidas'], 0.75)

print(30*'=')
media = np.mean(df)
mediana = np.median(df)

print(30*'=')
print('Q1:', q1)
print('Q2:', q2)
print('Q3:', q3)

print(30*'=')
print('Total de Unidades Vendidas:')
print(df['Unidades Vendidas'].sum())