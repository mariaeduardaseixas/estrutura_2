cpf = input("CPF: ")

soma = 0
for i in range(9):
    soma += int(cpf[i]) * (10 - i)

d1 = 11 - (soma % 11)
if d1 >= 10:
    d1 = 0

soma = 0
for i in range(10):
    soma += int(cpf[i]) * (11 - i)

d2 = 11 - (soma % 11)
if d2 >= 10:
    d2 = 0

if d1 == int(cpf[9]) and d2 == int(cpf[10]):
    print("CPF válido!")
else:
    print("CPF inválido!")