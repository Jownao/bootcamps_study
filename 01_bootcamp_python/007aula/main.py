from etl import ler_csv, calcular_vendas_categoria

# Desafio: Análise de Vendas de Produtos Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste em ler os dados, processá-los em um dicionário para análise e, por fim, calcular e reportar as vendas totais por categoria de produto.

path_arquivo = "vendas.csv"

print(calcular_vendas_categoria(ler_csv(path_arquivo)))