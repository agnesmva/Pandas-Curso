import pandas as pd

#Fazendo uma lista de idades 
#Esse seria o método tradicional de verificar uma média de idades 
idades = [18, 20, 22, 19, 21, 23, 25, 24, 26, 27]

#fazendo a média de idades
# media = sum(idades) /len(idades)
# print(f'Média: {media}')


#Agora fazendo utilizando series 
#o ideal é sempre trabalhar com variaveis do mesmo tipo
#por exemplo a series_idades é do tipo int64

series_idades = pd.Series(idades)

# print(series_idades)

print(series_idades.mean())
print(series_idades.var())
summary_idades = series_idades.describe()

print(summary_idades)

