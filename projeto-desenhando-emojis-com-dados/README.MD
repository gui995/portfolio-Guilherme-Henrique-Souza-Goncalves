
<div align="center">

# 🎨 Desenhando Emojis e Matrizes com Dados

**Engenharia de dados aplicada à computação visual e sonora**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-28a745?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Projeto-Acadêmico-orange?style=for-the-badge)

<br>

> *"Dados são apenas números — até você ensiná-los a desenhar."*

</div>

---

## 📌 Sobre o Projeto

Este projeto explora a **manipulação profunda de estruturas de dados aninhadas** em Python para processar imagens e áudio representados por matrizes.

O foco é demonstrar que por trás de qualquer imagem digital existe apenas **matemática pura** — e que com os algoritmos certos, é possível transformar dicionários e listas em elementos visuais e musicais completos.

```
📦 Dado bruto (número)
      ↓
🔢 Matriz numérica (lista de listas)
      ↓
🎨 Pixel colorido (canal RGB)
      ↓
🖼️ Imagem renderizada (plt.imshow)
```

---

## 🚀 Desafios e Funcionalidades

### 🟥 Desafio 1 — Processamento de Emojis RGB
> Aplicação de filtro de sombreamento em imagens representadas por dicionários

```python
# Percorre 3 níveis de profundidade: Dicionário → Linhas → Pixels
for emoji, linhas in emojis.items():
    for linha in linhas:
        for pixel in linha:
            pixel[0] //= 2  # Canal R
            pixel[1] //= 2  # Canal G
            pixel[2] //= 2  # Canal B
```

**O que faz:** Reduz a intensidade de cada canal de cor pela metade, criando um efeito de **sombra realista** sobre os emojis.

---

### 🟦 Desafio 2 — Transposição de Matrizes Musicais
> Reorganização de frequências sonoras de colunas para linhas

```python
# Converte estrutura de biblioteca musical
# DE:  instrumento → [frequência_por_tempo]
# PARA: tempo → [frequência_por_instrumento]
matriz_transposta = list(map(list, zip(*matriz_original)))
```

**O que faz:** Permite que os mesmos dados musicais sejam lidos em formatos diferentes — como tocar uma partitura de cima para baixo ou da esquerda para a direita.

---

### 🟩 Desafio 3 — Edição Dinâmica de Pixels
> Manipulação em tempo real de listas de cores

```python
galeria[0].pop(0)                    # Remove o primeiro pixel
galeria[0].insert(2, (0, 0, 255))    # Insere azul na posição 2
```

**O que faz:** Simula processos de **edição de imagem profissional** — equivalente ao que ferramentas como Photoshop fazem internamente, porém exposto em código puro.

---

## 🧠 Conceitos Aplicados

| Conceito | Onde foi usado |
|---|---|
| **Iteração multicamadas** | Navegação em dicionários 3 níveis abaixo |
| **Tuplas e listas aninhadas** | Estrutura dos canais RGB por pixel |
| **Transposição matricial** | Reorganização das frequências musicais |
| **Métodos de lista** | `.pop()` e `.insert()` para edição de pixels |
| **Visualização** | `plt.imshow()` para validar os resultados |
| **Operadores aritméticos** | Cálculo de intensidade de cor (`//= 2`) |

---

## 🛠️ Tecnologias

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white)
![Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

</div>

---

## 🚀 Como Executar

**Pré-requisitos:**
```bash
pip install matplotlib
```

**Opção 1 — Google Colab** *(recomendado para visualizar os gráficos)*
```
1. Acesse colab.research.google.com
2. Faça upload do arquivo .py
3. Execute célula por célula
```

**Opção 2 — VS Code / Terminal**
```bash
# Clone o repositório
git clone https://github.com/gui995/portfolio-guilherme-henrique-souza-goncalves

# Acesse a pasta
cd projeto-desenhando-emojis-com-dados

# Execute
python projeto_desenhando_emojis_com_dados.py
```

---

## 💡 Aprendizados

```
✅ Navegar em estruturas de dados 3+ níveis de profundidade
✅ Pensar em dados como matrizes — base da visão computacional
✅ Validar algoritmos visualmente com matplotlib
✅ Simular processos reais de edição de imagem com código puro
✅ Transpor matrizes para diferentes formatos de saída
```

---

## 👨‍💻 Autor

<div align="center">

**Guilherme Henrique Souza Gonçalves**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gui995)

[⬆️ Voltar ao Portfólio](https://github.com/gui995/portfolio-guilherme-henrique-souza-goncalves)

</div>
