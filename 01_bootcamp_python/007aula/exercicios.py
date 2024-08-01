from typing import List

# Calcular Média de Valores em uma Lista
def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

lista = [1, 2, 3, 4, 5]

print(calcular_media(lista))