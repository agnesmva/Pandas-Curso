import pandas as pd

df_transacoes = pd.read_csv("data/transactions.csv", sep=";")
renamed = {
    'IdTransaction': 'id',
    'IdCustomer' : 'id_costumer',
    'CreatedAt' : 'created_at',
    'VlPoints' : 'points',
    'DescSysOrigin' : 'system_origin'
}

df_transacoes.rename(columns=renamed, inplace=True)

df_transacoes[["id_costumer", "points"]]
##No pandas é possível retornar uma serie ou um dataframe
# caso eu busque pelo indice direto 

df_transacoes["id_costumer"] ##isso daqui me retorna uma série

df_transacoes[["id_costumer"]] ##isso me retorna um dataframe 

## Fazendo comparações com SQL 

#SELECT * from df_transacoes
df_transacoes

#SELECT id_costumer from df_transacoes
df_transacoes[["id_costumer"]]

#SELECT id_costumer, points FROM df_transacoes LIMIT 5 (usa os metodos head(), tail() ou sample())
df_transacoes[["id_costumer", "points"]].head(5)


#Reordenação de colunas ocorre com reatribução 
#exemplo 
print(df_transacoes.columns)
# retorna Index(['id', 'id_costumer', 'created_at', 'points', 'system_origin'], dtype='object')

#para fazer reordenação é possível castando para lista e usando os métodos de lista conhecidos, como sort()
colunas = list(df_transacoes.columns)
colunasOrdenadas = sorted(colunas)
df_transacoes = df_transacoes[colunasOrdenadas]
print(df_transacoes)