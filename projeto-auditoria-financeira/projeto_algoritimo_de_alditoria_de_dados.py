LIMITE_SEGURANCA = 10000.00
print(f"Limite de Segurança inicial: R$ {LIMITE_SEGURANCA:,.2f}")

# 2. Entrada de Dados e Casting
vendas = []
for i in range(1, 4):
    while True:
        try:
            valor_venda = input(f"Digite o valor da venda {i} do dia (ex: 1234.56): ").replace(',', '.')
            vendas.append(float(valor_venda))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

venda1, venda2, venda3 = vendas[0], vendas[1], vendas[2]
print(f"\nVenda 1: R$ {venda1:,.2f}")
print(f"Venda 2: R$ {venda2:,.2f}")
print(f"Venda 3: R$ {venda3:,.2f}")


# 3. Processamento Interno e Lógica de Investigação
def analisar_vendas(v1, v2, v3):
    global LIMITE_SEGURANCA

    print("\n--- Análise de Vendas ---")

    # Calcula a Média Simples
    media = (v1 + v2 + v3) / 3
    print(f"Média das vendas: R$ {media:,.2f}")

    # Verifica se a média ultrapassou o limite de segurança
    if media > LIMITE_SEGURANCA:
        print("⚠️  ALERTA: SISTEMA EM QUARENTENA!")

        # Verifica se alguma venda individual é 50% acima do limite
        if any(v > LIMITE_SEGURANCA * 1.5 for v in [v1, v2, v3]):
            print("📌 Sugestão: Vendas individuais muito altas.")
            print("   Considere ajustar o LIMITE_SEGURANCA se forem legítimas.")

            # Permite ajuste dinâmico pelo gerente
            resposta = input("\nGerente: Deseja atualizar o LIMITE_SEGURANCA? (s/n): ").strip().lower()
            if resposta == 's':
                while True:
                    try:
                        novo_limite = float(input("Digite o novo limite de segurança: ").replace(',', '.'))
                        LIMITE_SEGURANCA = novo_limite
                        print(f"✅ Limite atualizado para: R$ {LIMITE_SEGURANCA:,.2f}")
                        break
                    except ValueError:
                        print("Valor inválido. Tente novamente.")

    # Detecção de Discrepância (Outliers)
    discrepancia_detectada = False
    for venda in [v1, v2, v3]:
        if venda >= media * 5:
            print(f"🚨 ALERTA: Venda de R$ {venda:,.2f} é 5x maior que a média.")
            print("   Sugere-se REVISÃO MANUAL!")
            discrepancia_detectada = True

    if not discrepancia_detectada and media <= LIMITE_SEGURANCA:
        print("✅ Nenhuma anomalia detectada. Vendas dentro dos parâmetros.")

    return media


# Chamada da função
media_vendas = analisar_vendas(venda1, venda2, venda3)

# 4. Verificação de Tipos de Dados
print("\n--- Verificação de Tipos de Dados ---")
print(f"Tipo de LIMITE_SEGURANCA : {type(LIMITE_SEGURANCA)}")
print(f"Tipo de venda1           : {type(venda1)}")
print(f"Tipo de venda2           : {type(venda2)}")
print(f"Tipo de venda3           : {type(venda3)}")
print(f"Tipo da média das vendas : {type(media_vendas)}")
print(f"\nLIMITE_SEGURANCA atual   : R$ {LIMITE_SEGURANCA:,.2f}")
