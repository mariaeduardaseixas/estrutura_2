# 6. Desenvolva um programa que receba uma string e exiba a mesma na tela. Se o valor digitado for em branco exibir 'Dado inválido'
# Salvar o código como: validar_str.py

texto = input("Digite uma palavra/texto ou letra: ")

if texto == "" :
    print("Dado inválido")
else:
    print(f"O dado inserido foi {texto}")



