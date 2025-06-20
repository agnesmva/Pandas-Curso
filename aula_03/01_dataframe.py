import pandas as pd
import csv

df_clientes = pd.read_csv("data/customers.csv", sep=";")
## print(df_clientes.describe())

##para verificar as cinco primeiras linhas, apenas exibição 
# n é o limit que é usado para ver as primeiras linhad do data_frame
df_clientes.head(n = 10)

##para verificar os cinco últimos registros, apenas para exibição
# assim como head() o método tail consegue pegar n quantidades de linhas 
df_clientes.tail(10)

##pega amostras aleatórias de dados do dataset 

df_clientes.sample(10)


##Como verificar a quantidade de linhas e colunas? temos como saber a dimensão do dataframe por meio do atributo shape
##ele retorna uma tupla (qtd de linhas, qtd de colunas)
df_clientes.shape


#Aqui verifica o nome das colunas
df_clientes.columns


#Verifica os indices
df_clientes.index


#aqui temos no formato de string as informações do data frame, é possível adicionar atributos para saber o qto de ram está sendo consumido
df_clientes.info()

#retorna uma serie com as tipagens de cada coluna

df_clientes.dtypes