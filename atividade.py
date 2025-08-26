import os
os.system("cls// clear")

def calcular_valor_final():
    """
    Calcula o valor final de uma compra aplicando descontos cumulativos,
    com ambos os descontos baseados no valor original.
    """
    print(">>>>>>> LOJA DE ROUPAS ONLINE <<<<<<<")

    try:
        numero_compras_mes = int(input("Digite o número de compras que o cliente já fez este mês: "))
        valor_total_compra = float(input("Digite o valor total da compra atual (R$): ").replace(',', '.'))
    except ValueError:
        print("\nErro! Por favor, insira valores numéricos válidos.")
        return
    
    desconto_frequencia = 0.0
    desconto_valor = 0.0

    print("\n========= PROCESSANDO DESCONTOS =========")

    if numero_compras_mes >= 3:
        desconto_frequencia = valor_total_compra * 0.07
        print("Cliente frequente! Desconto de 7% aplicado.")

    if valor_total_compra > 500.00:
        desconto_valor = valor_total_compra * 0.10
        print("Compra acima de R$ 500,00! Desconto de 10% aplicado.")

    valor_final = valor_total_compra - desconto_frequencia - desconto_valor

    if desconto_frequencia == 0.0 and desconto_valor == 0.0:
        print("Nenhum desconto aplicável para esta compra.")

    print("\n========== RESUMO DA COMPRA ==========")
    print(f"Valor original da compra: R$ {valor_total_compra:.2f}")

    if desconto_frequencia > 0:
        print(f"Desconto por frequência (7%): R$ -{desconto_frequencia:.2f}")

    if desconto_valor > 0:
        print(f"Desconto por valor (10%):  R$ -{desconto_valor:.2f}")

    print("--------------------------------------")
    print(f"VALOR FINAL A PAGAR:      R$ {valor_final:.2f}")
    print("======================================")


if __name__ == "__main__":
    calcular_valor_final()