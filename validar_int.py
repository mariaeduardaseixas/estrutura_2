# 7. Desenvolva um programa que receba um inteiro e exiba o mesmo na tela. Se o valor digitado for em branco exibir 'Dado inválido'
# Salvar o código como: validar_int.py

inteiro = int(input("Digite um inteiro: "))

if inteiro == "":
    print("Dado inválido")
else:
    print(f"O valor inteiro é {inteiro}")