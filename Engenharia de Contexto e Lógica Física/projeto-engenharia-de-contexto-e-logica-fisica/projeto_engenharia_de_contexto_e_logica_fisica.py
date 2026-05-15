
import time

def analisar_microclima():
    """
    Função principal para executar a análise do microclima local.
    Dados baseados nas faixas oficiais do IQA adotadas pela CETESB (Brasil):
    0-40: Boa | 41-80: Moderada | 81-120: Ruim | >120: Muito Ruim/Péssima
    """
    # Armazenamento dos dados coletados em uma Lista de Listas
    # Estrutura interna: ["Nome do Local", Temperatura(°C), Umidade(%), IQA]
    dados_locais = [
        ["Av. Santo Amaro", 24, 75, 38],    # Região com corredor de ônibus e arborização
        ["Av. 23 de Maio", 27, 52, 85],     # Alto fluxo de veículos, vale poluído
        ["Radial Leste", 26, 58, 110]       # Altíssimo tráfego, pouca vegetação
    ]
    
    print("=" * 60)
    print("         RELATÓRIO DE MICROCLIMA URBANO - SÃO PAULO")
    print("=" * 60)
    
    # Loop para iterar sobre os locais
    for local in dados_locais:
        # Loop aninhado implícito/explícito para desempacotar as métricas do local
        nome = local[0]
        temp = local[1]
        umidade = local[2]
        iqa = local[3]
        
        # Estrutura match-case para classificar a Qualidade do Ar (IQA)
        match iqa:
            case _ if 0 <= iqa <= 40:
                classificacao_iqa = "Boa"
                risco_saude = "Ausente. Qualidade do ar ideal."
            case _ if 41 <= iqa <= 80:
                classificacao_iqa = "Moderada"
                risco_saude = "Pessoas sensíveis (crianças/idosos) podem apresentar sintomas leves."
            case _ if 81 <= iqa <= 120:
                classificacao_iqa = "Ruim"
                risco_saude = "População geral pode apresentar tosse seca e cansaço."
            case _:
                classificacao_iqa = "Muito Ruim / Péssima"
                risco_saude = "Sérios riscos respiratórios e cardiovasculares para toda a população."
                
        # Fórmula Autoral: Cálculo da Nota de Conforto Urbano (0 a 10)
        # Aplica operadores complexos e lógicos para penalizar extremos
        penalidade_temp = max(0, (temp - 22) * 0.4)
        penalidade_umidade = max(0, (60 - umidade) * 0.1)
        penalidade_iqa = (iqa / 150) * 4
        
        nota_conforto = 10 - (penalidade_temp + penalidade_umidade + penalidade_iqa)
        nota_conforto = max(0.0, min(10.0, nota_conforto))  # Garante os limites entre 0 e 10
        
        # Exibição dos resultados das métricas mapeadas
        print(f"\n📍 Local: {nome}")
        print(f"  -> Temperatura: {temp}°C | Umidade: {umidade}%")
        print(f"  -> IQA: {iqa} ({classificacao_iqa})")
        print(f"  -> Impacto à Saúde: {risco_saude}")
        print(f"  -> NOTA DE CONFORTO URBANO: {nota_conforto:.2f} / 10")
        print("-" * 60)

# Executar o algoritmo da Parte 1
if __name__ == "__main__":
    analisar_microclima()

def simular_evacuacao():
    # Duas Listas correspondentes: Uma com os nomes locais e outra com os estados/obstáculos
    locais = ["Escritório 2", "Escritório 1", "Escada 1", "Escada 2", "Estacionamento", "Portaria", "Rua"]
    estados = ["caminho livre", "chave", "fumaça", "porta trancada", "caminho livre", "seguro", "seguro"]
    
    # Variáveis de controle do agente e inventário
    posicao = 0
    energia = 20
    tem_chave = False
    
    print("=" * 60)
    print(" AGENTE INICIANDO ROTA DE EVACUAÇÃO DE EMERGÊNCIA ")
    print("=" * 60)
    
    # Loop while que representa a tentativa contínua do agente de evacuar
    while energia > 0:
        local_atual = locais[posicao]
        estado_atual = estados[posicao]
        
        print(f"\n[STATUS] Local atual: {local_atual} | Estado: {estado_atual} | Energia: {energia}")
        
        # Se chegou ao destino final (Rua), encerra o simulador
        if local_atual == "Rua":
            print("\n O agente chegou à rua com segurança!")
            break

        # Estrutura de decisão para avaliar o obstáculo do nó atual
        if estado_atual == "caminho livre":
            print("  O caminho está livre. O agente avança.")
            posicao += 1

        elif estado_atual == "fumaça":
            print("  Há fumaça no local, mas o agente consegue passar com cuidado.")
            posicao += 1
            energia -= 1

        elif estado_atual == "chave":
            print("  O agente encontrou uma chave.")
            tem_chave = True
            posicao += 1

        elif estado_atual == "porta trancada":
            print("  A saída está trancada.")

            # If aninhado para avaliar subcondições baseadas no inventário
            if tem_chave == True:
                print("  O agente tem a chave e conseguiu abrir a porta.")
                posicao += 1
            else:
                print("  O agente não tem a chave, então precisa voltar.")
                posicao -= 1  # Faz o agente retroceder na lista
                energia -= 1

        elif estado_atual == "seguro":
            print("  Local seguro.")
            posicao += 1

        # Garante que o agente não saia dos limites inferiores da lista
        if posicao < 0:
            posicao = 0

        # Garante que o agente não ultrapasse os limites superiores da lista
        if posicao >= len(locais):
            posicao = len(locais) - 1

        # Gasto básico de energia a cada iteração do loop
        energia -= 1

    # Condição de parada caso a energia acabe antes da saída
    if energia <= 0 and locais[posicao] != "Rua":
        print(f"\n O agente ficou sem energia em '{locais[posicao]}' antes de chegar à saída.")

# Executar o simulador da Parte 2
if __name__ == "__main__":
    simular_evacuacao()

Parágrafo 1: Durante o mapeamento físico do andar onde me encontro, que compreende a transição de salas de escritórios, escadarias internas e o estacionamento até a portaria, percebi que o ambiente real é repleto de nuances imperceptíveis no dia a dia, mas críticas em uma emergência. Elementos como a largura de uma escada, a presença de uma porta corta-fogo pesada ou áreas amplas como o estacionamento não se comportam como simples pontos estáticos. Eles oferecem atritos mecânicos e dinâmicos que mudam drasticamente o ritmo de qualquer deslocamento, mostrando que a realidade física é fluida e caótica.

Parágrafo 2: Ao tentar transformar portas, escadas e corredores em variáveis lógicas e listas estruturadas, o maior desafio foi reduzir a imprevisibilidade de eventos físicos a estados booleanos ou condicionais exatos (if/else). Um obstáculo real como a fumaça ou uma porta trancada envolve fatores complexos na vida real. No entanto, para que o computador pudesse processá-lo, precisei traduzir essa ameaça em uma perda quantificável de energia, em verificações condicionais e em um gatilho de inventário (possuir ou não o booleano tem_chave). Essa modelagem exige uma simplificação cirúrgica, onde o ruído do mundo real é descartado para dar lugar a regras matemáticas estritas de causa e efeito.

Parágrafo 3: Isso me fez refletir que, no meu dia a dia, aprender a programar me ajuda a enxergar problemas complexos fora das telas não mais como barreiras monolíticas e intransponíveis, mas como sistemas integrados por múltiplos subproblemas menores. Passar pelo processo de "quebrar" a realidade me dá a capacidade analítica de mapear rotas alternativas diante de imprevistos cotidianos, antecipar "gargalos" nas minhas tarefas diárias e gerenciar meus recursos (como tempo e foco) de forma muito semelhante a um algoritmo. A programação, portanto, reconfigura a mente para substituir o desespero do caos pela frieza do planejamento lógico estruturado.

