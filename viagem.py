# 3. Desenvolva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
# 0,45 para viagens mais longas.
# Salvar o código como: viagens.py

distancia = float(input("Insira a distância que deseja pecorrer: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"O valor total a ser pago será {preco}")