# 4. Suponha que o professor Atila possua dois logins na rede do SENAI-SP. 
# Construa um programa que valide o acesso do professor à rede. 
# Caso o par usuário/senha informado esteja correto, o programa deve imprimir a mensagem “Seja bem vindo!”.
# Caso contrário, “Usuário e senha não conferem”.
# Dados dos dois logins:
# login 1			login 2
# usuário: atila		usuário: olivi
# senha: 12345		senha: 54321
# Salvar o código como: dois_logins.py

usuario = str(input("Digite o usuário para realizar o login:"))
senha = input("Digite a senha: ")

print("LOGIN 1")

if usuario == "atila" or senha == 12345:
    print("Seja bem-vindo!!")
else:
    print("Usuário e senha não conferem")

usuario2 = str(input("Digite o segundo usuário que irá realizar o login:"))
senha2 = input("Digite a senha:")

print("LOGIN 2")

if usuario2 == "olivi" or senha2 == 54321:
    print("Seja bem-vindo!")
else:
    print("Usuário e senha não conferem")