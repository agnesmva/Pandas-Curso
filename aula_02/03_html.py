import pandas as pd


url = "https://pt.wikipedia.org/wiki/Direitos_LGBT_no_Brasil"
df_list = pd.read_html(url)

# Pegando a terceira tabela (índice 2)
df = df_list[2]
df.to_csv("TabelaDireitos.csv", sep=";", index=False)

