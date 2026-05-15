emoji_data = {
    "nome": "Smile",
    "grade": [
        [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)],
        [(255, 255, 0), (0, 0, 0),     (255, 255, 0), (0, 0, 0),     (255, 255, 0)],
        [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)],
        [(255, 255, 0), (0, 0, 0),     (0, 0, 0),     (0, 0, 0),     (255, 255, 0)],
        [(255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0), (255, 255, 0)],
    ]
}

# Nível 1 — percorre o dicionário (chave: valor)
for chave, valor in emoji_data.items():

    if chave == "grade":  # só processa a grade, ignora o "nome"

        nova_grade = []  # vai guardar as linhas já processadas

        # Nível 2 — percorre cada linha da grade
        for linha in valor:

            nova_linha = []  # vai guardar os pixels já processados

            # Nível 3 — percorre cada pixel (tupla RGB) da linha
            for pixel in linha:

                if pixel == (255, 255, 0):  # pixel amarelo?
                    # Tuplas são imutáveis → cria uma nova com brilho reduzido
                    pixel_sombra = (pixel[0] // 2, pixel[1] // 2, pixel[2] // 2)
                    nova_linha.append(pixel_sombra)
                else:
                    nova_linha.append(pixel)  # pixel preto: mantém igual

            nova_grade.append(nova_linha)  # adiciona a linha processada

        emoji_data["grade"] = nova_grade  # atualiza a grade no dicionário

# Exibe o resultado
print(f"Emoji: {emoji_data['nome']}")
print()
for i, linha in enumerate(emoji_data["grade"]):
    print(f"Linha {i}: {linha}")
