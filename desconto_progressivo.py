"""
Sistema de desconto progressivo - Loja Online
Solicita o valor total da compra e aplica um desconto de acordo
com faixas de valor, exibindo o valor do desconto e o valor final a pagar.
"""


def calcular_percentual_desconto(valor_compra):
    """
    Recebe o valor total da compra e retorna o percentual de desconto
    (em decimal) correspondente à faixa de valor, de acordo com as regras:
        - menor que 200:            5%
        - entre 200 (incluso) e 300: 10%
        - 300 ou mais:               15%
    """
    if valor_compra < 200:
        percentual = 0.05
    elif valor_compra < 300:  # já sabemos que valor_compra >= 200 aqui
        percentual = 0.10
    else:  # valor_compra >= 300
        percentual = 0.15

    return percentual


def calcular_valores(valor_compra, percentual_desconto):
    """
    Recebe o valor da compra e o percentual de desconto (decimal)
    e retorna uma tupla com (valor_do_desconto, valor_final_a_pagar).
    """
    valor_desconto = valor_compra * percentual_desconto
    valor_final = valor_compra - valor_desconto

    return valor_desconto, valor_final


def exibir_resultado(valor_compra, percentual_desconto, valor_desconto, valor_final):
    """
    Exibe, de forma formatada, o resumo da compra: valor original,
    percentual e valor do desconto aplicado e o valor final a pagar.
    """
    print("\n----- Resumo da compra -----")
    print(f"Valor da compra:   R$ {valor_compra:.2f}")
    print(f"Desconto aplicado: {percentual_desconto * 100:.0f}%  (R$ {valor_desconto:.2f})")
    print(f"Valor a pagar:     R$ {valor_final:.2f}")
    print("-----------------------------\n")


def obter_valor_compra():
    """
    Solicita ao usuário o valor total da compra e garante que o valor
    informado seja numérico e não negativo antes de devolvê-lo.
    """
    while True:
        entrada = input("Digite o valor total da compra: R$ ")
        try:
            valor = float(entrada.replace(",", "."))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Digite apenas números (ex: 250.90).")


def main():
    """Função principal: orquestra a leitura, o cálculo e a exibição do resultado."""
    valor_compra = obter_valor_compra()

    percentual_desconto = calcular_percentual_desconto(valor_compra)
    valor_desconto, valor_final = calcular_valores(valor_compra, percentual_desconto)

    exibir_resultado(valor_compra, percentual_desconto, valor_desconto, valor_final)


if __name__ == "__main__":
    main()
