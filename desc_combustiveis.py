# 8. Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#    Álcool:
#       até 20 litros, desconto de 3% por litro
#       acima de 20 litros, desconto de 5% por litro 
#    Gasolina:
#       até 20 litros, desconto de 4% por litro
#       acima de 20 litros, desconto de 6% por litro 

# O programa deverá ler o número de litros vendidos, o tipo de combustível codificado da seguinte forma: 
#    A - Álcool, 
#    G - Gasolina, 
# Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4,95 o preço do litro do álcool é R$ 2,89.
# Salvar o código como: desc_combustiveis.py

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A - álcool/ G - gasolina): ")
preco_gasolina = 4.35
preco_alcool = 2.89



if litros <= 20 or tipo == "A":
    desconto = litros * preco_gasolina * 3 / 100
elif litros > 20 or tipo == "A":
    desconto = litros * preco_gasolina * 5 / 100
elif litros <= 20 or tipo == "G":
    desconto = litros * preco_alcool * 4 / 100
elif litros > 20 or tipo == "G":
    desconto = litros * preco_alcool * 6 /100

valor_total = litros - desconto
print(f"O valor total que será gasto é de R$ = {valor_total}")

