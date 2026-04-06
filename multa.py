# 1. Desenvolva um programa que pergunte a velocidade do carro de um usuário. 
# Se a velocidade ultrapassar 80km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 50,00 por cada km acima de 80 km/h.
# Exemplo: Digite a velocidade em Km/h: 85
# Limite = 80Km/h
# Excedeu 5Km/h
# multa = 5Km/h * R$ 50,00
# Valor da multa: R$ 250,00
# Salvar o código como: multa.py

velocidade = float(input("Digite a velocidade do carro em Km/h : "))
limite = velocidade - 80

if velocidade > 80:
    multa = limite * 50
else:
    print("Não conteve multa!continue assim!")

print(f"A velocidade do carro foi de {velocidade}")
print(f"O carro andou {limite} a mais do que o necessário")
print(f"O valor da multa de será paga é de {multa}")
