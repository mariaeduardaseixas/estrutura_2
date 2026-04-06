# 5. Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu estoque em promoção, de acordo com a tabela a seguir:

# Código	Condição de Pagamento	Desconto (%)
# 1 	À vista (em espécie) 	10
# 2	Cartão de débito	5
# 3	Cartão de crédito	3
# 4	PIX			7.5

# Construa um programa que solicite ao operador do caixa o preço total da venda, bem como a forma de pagamento.
# Ao fim, o programa deve informar o valor final a ser pago.
# Salvar o código como: black_friday.py

condicao = str(input("Insira a condição de pagamento: "))
preco = float(input("Digite o preço do produto"))


if condicao == "a vista":
    valor = preco * 10 /100
elif condicao == "cartão de débito":
    valor = preco * 5 / 100
elif condicao == "cartão de débito":
    valor = preco * 3 /100
elif condicao == "PIX":
    valor = preco * 7.5 /100
else:
    print("Não há possibilidades de outras maneiras de pagamento")

valor_total = preco - valor
print(f"O valor total a ser pago é {valor_total:.2f}")