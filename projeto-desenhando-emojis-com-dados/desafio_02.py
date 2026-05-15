biblioteca_musical = {
    "Toques": [
        {"Alegre": ([440, 480], [520, 560])},
        {"Triste": ([200, 150], [100, 50])}
    ]
}

# Nível 1 — percorre a lista de toques
for toque in biblioteca_musical["Toques"]:

    # Nível 2 — percorre o dicionário de cada toque (ex: {"Alegre": ...})
    for nome, matriz in toque.items():

        # Monta a matriz transposta manualmente (sem zip, sem numpy)
        # matriz tem 2 linhas e 2 colunas → transposta também é 2x2
        transposta = []

        # Nível 3 — percorre os índices das COLUNAS (que viram linhas)
        for coluna in range(len(matriz[0])):  # range(2) → 0, 1

            nova_linha = []

            for linha in range(len(matriz)):  # range(2) → 0, 1
                nova_linha.append(matriz[linha][coluna])

            transposta.append(tuple(nova_linha))  # mantém como tupla igual ao original

        # .update() substitui o valor da chave existente no dicionário
        toque.update({nome: transposta})

# Exibe o resultado
print("=== Matrizes Transpostas ===\n")
for toque in biblioteca_musical["Toques"]:
    for nome, matriz in toque.items():
        print(f"{nome}:")
        for linha in matriz:
            print(f"  {list(linha)}")
        print()
