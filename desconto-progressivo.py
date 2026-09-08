# Programa de Desconto Progressivo - Loja Online

# Regras de desconto:
# - Compra menor que R$ 200,00 -> desconto de 5%
# - Compra maior ou igual a R$ 200,00 e menor que R$ 300,00 -> desconto de 10%
# - Compra maior ou igual a R$ 300,00 -> desconto de 15%

# Solicita ao usuário o valor total da compra e converte para float
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica a faixa de valor e define o PERCENTUAL de desconto correspondente.

if valor_compra < 200:
    percentual_desconto = 5
elif valor_compra < 300:
    percentual_desconto = 10
else:
    percentual_desconto = 15

# Calcula o valor do desconto com base no percentual definido acima
valor_desconto = valor_compra * (percentual_desconto / 100)

# Calcula o valor final que o cliente vai pagar
valor_final = valor_compra - valor_desconto

# Exibe o resumo da compra para o usuário
print("\n--- Resumo da compra ---")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual_desconto}% (R$ {valor_desconto:.2f})")
print(f"Valor total a pagar: R$ {valor_final:.2f}")