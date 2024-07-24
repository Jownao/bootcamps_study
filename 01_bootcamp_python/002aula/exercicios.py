# Exercício 2: Resto da Divisão por 5
# num = int(input("Digite um número: "))
num = 18  # Exemplo de entrada
resultado_resto = num % 5
print("O resto da divisão por 5 é:", resultado_resto)

# Exercício 10: Área de um Círculo
# raio = float(input("Digite o raio do círculo: "))
raio = 5.0  # Exemplo de entrada
area = 3.14159 * raio ** 2
print("A área do círculo é:", area)

# Exercício 14: Separar Dia, Mês e Ano de uma Data
# data = input("Digite uma data no formato dd/mm/aaaa: ")
data = "01/01/2024"  # Exemplo de entrada
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)


# Type error

# Exemplo que causa TypeError
try:
    resultado = len(5)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro


# Type Check

# Exemplo de Type Check
# Para verificar o tipo de uma variável em Python, você pode usar a função type() ou isinstance().

numero = 10
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")

# Type Conversion

# Exemplo de Type Conversion
# Se você quiser somar um inteiro e um número flutuante, pode ser necessário converter o inteiro para flutuante ou vice-versa para garantir que a operação de soma seja realizada corretamente.

numero_inteiro = 5
numero_flutuante = 2.5
# Converte o inteiro para flutuante e realiza a soma
soma = float(numero_inteiro) + numero_flutuante
print(soma)  # Resultado: 7.5

# try-except

# Exemplo de try-except
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")

# Exercício 23: Calculadora Simples


try:
    input1 = float(input("Digite o primeiro número: "))
    input2 = float(input("Digite o segundo número: "))

    operacao = input("Digite o operador (+,-,*,/): ")

    if operacao == "+":
        resultado = input1 + input2
    elif operacao == "-":
        resultado = input1 - input2
    elif operacao == "*":
        resultado = input1 * input2
    elif operacao == "/":
        resultado = input1 / input2
except:
    print("Digite um número válido.")

# Exercício 24: Classificador de Números

try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")