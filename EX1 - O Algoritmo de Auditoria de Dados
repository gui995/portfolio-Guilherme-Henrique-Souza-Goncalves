import time

# 1. Configuração Global 
LIMITE_SEGURANCA = 10000.00 
print(f"Limite de Segurança inicial: R$ {LIMITE_SEGURANCA:,.2f}") 

# 2. Entrada de Dados e Casting 
# Certifica que o programa aceite números decimais e substitui ',' por '.'
vendas = [] 
for i in range(1, 4): 
    while True: 
        try: 
            # O Colab exibirá uma caixa de texto para cada input
            valor_venda = input(f"Digite o valor da venda {i} do dia (ex: 1234.56): ").replace(',', '.') 
            vendas.append(float(valor_venda)) 
            break 
        except ValueError: 
            print("❌ Entrada inválida. Por favor, digite um número.") 

venda1, venda2, venda3 = vendas[0], vendas[1], vendas[2] 

print(f"\n✅ Venda 1: R$ {venda1:,.2f}") 
print(f"✅ Venda 2: R$ {venda2:,.2f}") 
print(f"✅ Venda 3: R$ {venda3:,.2f}") 

# 3. Processamento Interno e Lógica de Investigação 
def analisar_vendas(v1, v2, v3): 
    global LIMITE_SEGURANCA 

    print("\n" + "="*30)
    print("--- ANÁLISE DE VENDAS ---") 
    print("="*30)

    # Calcula a Média Simples 
    media = (v1 + v2 + v3) / 3 
    print(f"Média das vendas: R$ {media:,.2f}") 

    # Lógica de Investigação 
    if media > LIMITE_SEGURANCA: 
        print("⚠️ ALERTA: SISTEMA EM QUARENTENA!") 
        if any(v > LIMITE_SEGURANCA * 1.5 for v in [v1, v2, v3]): 
            print("💡 Sugestão: Vendas individuais muito altas. Considere ajustar o LIMITE_SEGURANCA.") 

    discrepancia_detectada = False 
    for venda in [v1, v2, v3]: 
        if venda >= media * 5: 
            print(f"🚨 ALERTA: Venda de R$ {venda:,.2f} é 5x maior que a média. REVISÃO MANUAL!") 
            discrepancia_detectada = True 

    if not discrepancia_detectada and media <= LIMITE_SEGURANCA: 
        print("✔️ Nenhuma anomalia grave detectada. Parâmetros normais.") 
     
    return media 

# Chamada da função 
media_vendas = analisar_vendas(venda1, venda2, venda3) 

# 4. Apresentação técnica
print("\n" + "-"*30)
print("--- VERIFICAÇÃO DE TIPOS (AUDITORIA) ---") 
print(f"Tipo LIMITE_SEGURANCA: {type(LIMITE_SEGURANCA)}") 
print(f"Tipo venda1-3: {type(venda1)}") 
print(f"Tipo média: {type(media_vendas)}") 
print(f"\nO LIMITE_SEGURANCA final é: R$ {LIMITE_SEGURANCA:,.2f}")
