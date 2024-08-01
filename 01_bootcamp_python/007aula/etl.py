import csv

def ler_csv(nome_arquivo: str) -> list[dict]:
    """Função para ler um arquivo CSV e retornar uma lista de dicionários com os dados lidos."""
    lista_dados = []
    with open(nome_arquivo, "r",encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista_dados.append(linha)
    return lista_dados
        
#print(ler_csv(path_arquivo))

#Calcular o total de vendas (Quantidade * Venda) por categoria.
def calcular_vendas_categoria(lista_dados):
    """Função para calcular o total de vendas por categoria."""
    vendas_por_categoria = {}
    for dado in lista_dados:
        categoria = dado["Categoria"]
        quantidade = int(dado["Quantidade"])
        venda = float(dado["Venda"])
        if categoria not in vendas_por_categoria:
            vendas_por_categoria[categoria] = 0
        vendas_por_categoria[categoria] += quantidade * venda
    return vendas_por_categoria