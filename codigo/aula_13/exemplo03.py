import numpy as np
dados_salario = [2500, 3500, 4000, 30000, 2000, 3000]

# media
media = np.mean(dados_salario)
print('Média:', media)

# mediana: a mediana com o numpy ajuda a ordenar os dados na ordem
# crescente que é assim q calculamos a mediana
mediana = np.median(dados_salario)
print('Mediana:', mediana)
