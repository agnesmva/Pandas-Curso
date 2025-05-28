import pandas as pd

idades = [18, 15, 22, 19, 85, 23, 25, 20, 26, 36, 40, 40]
nomes = ["Maria", "Jonathan", "Danubio","Celso", "Noite", "Daniel", "Ulices", "Jonathan", "Jose", "Joao", "Rose", "Lady"]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

#O Dataframe pode ser pensado como um "varal" que pendura a serie nele. O dataframe extendemos os dados das series nele.
#Trata-se então de um conjunto de series. 
#O dataframe possui linhas e colunas - "como se fosse uma planilha"
#Onde cada coluna é uma serie

data_frame = pd.DataFrame()
data_frame["idade"] = series_idades
data_frame["nome"] = series_nomes



## Acessando o dataframe

##Acessando uma coluna
data_frame["idade"] # retorna a coluna idade, o series idade
data_frame_ordernado = data_frame.sort_values( by="idade")

print(data_frame_ordernado.iloc[-1])  # retorna uma serie em nível de linha

