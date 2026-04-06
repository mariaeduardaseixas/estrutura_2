# 4. Uma empresa, que presta serviço à companhia de energia elétrica do estado, necessita de um programa que auxilie os seus eletricistas no cálculo das principais grandezas da Eletricidade
# que são Tensão, Resistência e Corrente. Sabe-se que:
# U = R * I, 
# onde, 
# U é a Tensão      (em V), 
# R é a Resistência (em Ώ) e,
# I é a Corrente    (em A).

# Você foi contratado(a) pela empresa para atender a essa solicitação.
# Construa um programa que apresente o seguinte menu:

# ******************************
# CÁLCULO DE GRANDEZAS ELÉTRICAS
# ******************************
# 1. Tensão (em Volt)
# 2. Resistência (em Ohm)
# 3. Corrente (em Ampére)
# 4. Sair do programa
# ******************************
# Qual grandeza deseja calcular?

# Em seguida, o programa deve solicitar que o eletricista informe o valor das outras duas grandezas para realizar o cálculo.

# Quando o eletricista escolher:
# 1. Tensão, o programa deve solicitar que ele informe os valores da Resistência e da Corrente.
#    Utilizar a fórmula: U = R * I

# 2. Resistência, o programa deve solicitar que ele informe os valores da Tensão e da Corrente.
#    Utilizar a fórmula: R = U / I

# 3. Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência.
#    Utilizar a fórmula: I = U / R

# Por fim, o programa deve calcular e apresentar o valor encontrado para a grandeza escolhida.
# Obs.: Qualquer opção diferente das apresentadas no menu (1 a 4) deverão ser informadas ao usuário como 'Opção inválida!'
# Salvar o código como: grandezas.py////

print("CÁLCULO DE GRANDEZAS ELÉTRICAS")


print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("4. Sair do programa")


opcao = int(input("Qual grandeza deseja calcular? "))

if opcao == 1:
    # Tensão
    r = float(input("Informe a Resistência (Ohm): "))
    i = float(input("Informe a Corrente (Ampére): "))
    u = r * i
    print(f"Tensão (U) = {u:.2f} V")

elif opcao == 2:
    # Resistência
    u = float(input("Informe a Tensão (Volt): "))
    i = float(input("Informe a Corrente (Ampére): "))
    if i != 0:
        r = u / i
        print(f"Resistência (R) = {r:.2f} Ohm")
    else:
        print("Erro: Corrente não pode ser zero!")

elif opcao == 3:
    # Corrente
    u = float(input("Informe a Tensão (Volt): "))
    r = float(input("Informe a Resistência (Ohm): "))
    if r != 0:
        i = u / r
        print(f"Corrente (I) = {i:.2f} A")
    

elif opcao == 4:
    print("Encerrando o programa...")
else:
    print("Opção inválida")
    



