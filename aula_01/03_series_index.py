import pandas as pd

idades = [18, 15, 22, 19, 85, 23, 25, 20, 26, 36, 40, 40]
indices = ["Maria", "Jonathan", "Jose","Maria", "Jonathan", "Jose", "Maria", "Jonathan", "Jose", "Joao", "Rose", "Lady"]

series_idades = pd.Series(idades)
# print(series_idades)
## mesmo que escrever series_idades.loc (default)

#os indices das séries funcionam da mesma maneira que chaves no dicionário 
#logo não é possível fazer series_idades[-1], pois, normalmente não vai existir essa chave
#o index sempre fica vínculado a linha da serie

#series_ordernados = series_idades.sort_values()
# print(series_ordenados)


series_idades_novoIndex = pd.Series(idades, index=indices)
## Como acessar o elemento independente do index
## Quando usamos iloc usamos o index como posição, não como chave
series_idades.iloc[-1]
print("Usando Slice:\n",series_idades_novoIndex.iloc[:3]) #usandi slice como se fossem listas
print("Acessando a primeira posição:\n",series_idades_novoIndex.iloc[0]) #acessando pela posição do index, não pela chave
print("Acessando o último elemento:\n", series_idades_novoIndex.iloc[-1]) #acessando o último elemento
print("Reverse:\n", series_idades_novoIndex.iloc[:: -1]) #fazendo um "reverse"