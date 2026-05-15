# Desafio 3 — O Integrador (Criação Livre)
# Playlist de figurinhas do WhatsApp (tipo um sticker pack)
# Cada figurinha tem um nome, uma "vibe" e os pixels da carinha

sticker_pack = {
    "pack": "Figurinhas da Galera",
    "figurinhas": [
        {
            "nome": "Chapolin",
            "vibe": "zoeira",
            "pixels": [
                (255, 0, 0),    # vermelho
                (255, 165, 0),  # laranja
                (255, 255, 0),  # amarelo
            ]
        },
        {
            "nome": "Caveirinha",
            "vibe": "dark",
            "pixels": [
                (30, 30, 30),
                (80, 80, 80),
                (200, 200, 200),
            ]
        }
    ]
}

# Remove a última figurinha e insere uma nova
sticker_pack["figurinhas"].pop()
sticker_pack["figurinhas"].insert(1, {
    "nome": "Sapo Frog",
    "vibe": "relax",
    "pixels": [
        (0, 180, 0),
        (0, 220, 80),
        (180, 255, 100),
    ]
})

vibes_contadas = {}  # conta quantas figurinhas tem de cada vibe

print(f"=== {sticker_pack['pack']} ===\n")

# Nível 1 — chaves do dicionário principal
for chave in sticker_pack.keys():
    if chave != "figurinhas":
        continue

    # Nível 2 — cada figurinha
    for fig in sticker_pack["figurinhas"]:
        v = fig["vibe"]

        # Conta as vibes (tipo um groupby na mão)
        if v not in vibes_contadas:
            vibes_contadas[v] = 0
        vibes_contadas[v] += 1

        print(f"[ {fig['nome']} ] — vibe: {v}")

        # Nível 3 — cada cor dos pixels
        for i, pixel in enumerate(fig["pixels"]):
            r, g, b = pixel  # desempacota a tupla
            brilho = (r + g + b) // 3
            print(f"  pixel {i+1}: RGB({r},{g},{b}) | brilho médio: {brilho}")

        print()

print("Vibes do pack:", vibes_contadas)
