# Sistema de Desconto Progressivo - Loja Online

Programa em Python desenvolvido como atividade de recuperação, que calcula o desconto de uma compra em uma loja online de acordo com o valor total informado pelo cliente, aplicando regras de desconto progressivo.

## Regras de desconto

| Valor da compra              | Desconto |
|-------------------------------|----------|
| Menor que R$ 200,00            | 5%       |
| De R$ 200,00 até R$ 299,99     | 10%      |
| A partir de R$ 300,00          | 15%      |

## Como executar

Pré-requisito: [Python 3](https://www.python.org/) instalado.

```bash
python3 desconto_progressivo.py
```

O programa solicitará o valor total da compra e exibirá o percentual e o valor do desconto aplicado, além do valor final a pagar.

### Exemplo de execução

```
Digite o valor total da compra: R$ 250

----- Resumo da compra -----
Valor da compra:   R$ 250.00
Desconto aplicado: 10%  (R$ 25.00)
Valor a pagar:     R$ 225.00
-----------------------------
```

## Estrutura do código

O código foi dividido em funções, cada uma com uma única responsabilidade:

- `obter_valor_compra()` — solicita e valida o valor digitado pelo usuário (impede texto ou números negativos).
- `calcular_percentual_desconto(valor_compra)` — define, por meio de estrutura condicional (`if/elif/else`), qual percentual de desconto se aplica à faixa de valor.
- `calcular_valores(valor_compra, percentual_desconto)` — calcula o valor do desconto e o valor final a pagar.
- `exibir_resultado(...)` — imprime o resumo da compra formatado.
- `main()` — organiza a chamada das demais funções.

Essa organização evita repetição de código e deixa cada etapa do processo (entrada, regra de negócio, cálculo e saída) isolada e fácil de testar.

## Conceitos aplicados

- Entrada e validação de dados (`input`, `try/except`, `while`)
- Estrutura condicional `if/elif/else`
- Programação estruturada em funções
- Formatação de saída (f-strings)

## Prints de funcionamento

<img src="img/print_terminal_150" alt="Demonstração Fiscore" width="100%"/>
<img src="img/print_terminal_250" alt="Demonstração Fiscore" width="100%"/>
<img src="img/print_terminal_450" alt="Demonstração Fiscore" width="100%"/>

## Autor

Atividade desenvolvida por Nicholas Vieira de Souza
