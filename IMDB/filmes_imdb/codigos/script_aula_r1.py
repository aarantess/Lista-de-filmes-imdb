# Script para análise de dados do IMDB

# Importando as bibliotecas necessárias
import pandas as pd

# saudacao = "Olá, seja bem-vindo à análise de dados do IMDB!"
# print(saudacao)

"""['id_filme', 'titulo', 'ano_lancamento', 'genero', 'duracao_min', 'rating_imdb', 'orcamento_milhoes', 'data_lancamento', 'bilheteria_dolares', 'nome_pais', 'continente', 'idioma_principal', 'moeda', 'capital', 'nome_produtora', 'ano_fundacao', 'pais_sede']"""

caminho_arquivo = "C:\\projects\\IMDB\\filmes_imdb\\dados\\filmes_imdb.xlsx"

df_imdb = pd.read_excel(caminho_arquivo) #Transformando o arquivo excel em um DataFrame

print(df_imdb.head(10)) #Exibindo as primeiras linhas do DataFrame para verificar se os dados foram carregados corretamente

print(df_imdb.info()) #Exibindo informações sobre o DataFrame, como número de linhas, colunas e tipos de dados

print(df_imdb.shape) #Exibindo o número de linhas e colunas do DataFrame

print(df_imdb.columns.tolist()) #Exibindo os nomes das colunas do DataFrame em formato de lista

#to_save
 
df_imdb.to_csv("C:\\projects\\IMDB\\filmes_imdb\\dados\\dados_csv\\tab_imdb.csv", index=False) #Salvando o DataFrame em formato CSV, sem incluir o índice das linhas


df_imdb.to_excel("C:\\projects\\IMDB\\filmes_imdb\\dados\\dados_excel\\tab_imdb.xlsx", index=False) #Salvando o DataFrame em formato Excel, sem incluir o índice das linhas

print("Análise de dados do IMDB concluída com sucesso!")