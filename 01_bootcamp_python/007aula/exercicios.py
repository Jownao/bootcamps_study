from typing import List

# Calcular Média de Valores em uma Lista
def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

lista = [1.3, 2, 3, 4, 5]

print(calcular_media(lista))

# Filtrar Dados Acima de um Limite
def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

print(filtrar_acima_de(lista,3))

# Converter Celsius para Fahrenheit em uma Lista
def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]