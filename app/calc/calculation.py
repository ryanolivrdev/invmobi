import math

def valores_pago(valor_pago_mes: [], tempo: int, taxa):
    total = 0
    tempo = math.ceil(tempo/12)
    for i in range(1, tempo):
        num = valor_pago_mes[i - 1] * (1 + taxa / 100)
        valor_pago_mes.append(num)
        total += num * 12
    return total


def comparando_tempo(aluguel, valor_compra, entrada, taxa_financiamento, taxa_aluguel, tempo):
    total_pago_compra = ((valor_compra - entrada) * (1 + (taxa_financiamento / 100)) ** (tempo/12)) + entrada
    total_pago_aluguel = 0
    anos = 1
    teste = aluguel
    while total_pago_compra > total_pago_aluguel:
        teste = teste * (1 + taxa_aluguel / 100)
        total_pago_aluguel += teste * 12
        anos += 1
        
    return  [total_pago_aluguel, total_pago_compra,anos]


# calcular(600000,150000,10,2000,8.5,11)

def calcular(valor_compra,
             valor_entrada,
             tempo,
             valor_aluguel,
             valorizacao_imovel,
             taxa_financiamento):
    total_pago_ano_compra = ((valor_compra - valor_entrada) * (1 + (taxa_financiamento / 100)) ** (tempo/12)) + valor_entrada
    valor_pago_mes_compra = total_pago_ano_compra / (tempo)

    valor_pago_mes_aluguel = [valor_aluguel]
    total_pago_ano_aluguel = valores_pago(valor_pago_mes_aluguel, tempo, valorizacao_imovel)

    print(comparando_tempo(2000, 600000, 150000, 11, 8.5, 120))


# calcular(600000, 150000, 10, 2000, 8.5, 11)