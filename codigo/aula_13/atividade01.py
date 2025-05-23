import numpy as np

v_imoveis = np.array([150, 180, 200, 220, 250, 280, 300, 320, 400, 1500])

media = np.mean(v_imoveis)
print(f"Média: {media}00")

mediana = np.median(v_imoveis)
print(f"Mediana: {mediana}00")

print(f"O valor que mais justifica o valor das casas é a mediana:{mediana}00")