
# 2. Desenvolva um programa que leia três números e que imprima:
#    2.1. o maior,
#    2.2. o menor,
#    2.3. a soma,
#    2.4. a média.
# Exemplo:
# num1 = 5	num2 = 3	num3 = 10
# **********
# maior = 10
# menor = 3
# soma = 18
# media = 6
# Salvar o código como: maior_menor.py

num1 = float(input("Digite o valor do primeiro número: "))
num2 = float(input("Digite o valor do segundo número: "))
num3 = float(input("Digite o valor do terceiro número: "))

lista = [num1, num2, num3]

print("O maior valor")
print(max(lista))

print("O menor valor")
print(min(lista))

print("A soma dos valores")
print(sum(lista))

print("A média dos valores")
media = num1 + num2 + num3 / 3
print(f"A média é de {media:.2f}")