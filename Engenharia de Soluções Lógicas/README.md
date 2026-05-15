
<div align="center">

# 🌱 Sistema Inteligente de Irrigação Automatizada

**Engenharia de Soluções Lógicas aplicada ao Agronegócio**

![Python](https://img.shields.io/badge/Lógica-Pseudocódigo-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-28a745?style=for-the-badge)
![Tipo](https://img.shields.io/badge/Projeto-Acadêmico-orange?style=for-the-badge)

<br>

> *"A lógica de programação transforma sensores em inteligência — e inteligência em economia de recursos."*

</div>

---

## 📌 Sobre o Projeto

Este projeto apresenta a **solução lógica completa** de um sistema automatizado de irrigação, desenvolvido a partir de duas entregas complementares:

- 📝 **Pseudocódigo** — representação estruturada da lógica em linguagem próxima ao humano
- 📊 **Fluxograma** — representação visual do fluxo de decisões e ações do sistema

O sistema monitora continuamente a umidade do solo e o fluxo de água, tomando decisões autônomas para **ativar, manter ou desligar** a irrigação — além de emitir alertas em caso de desperdício ou vazamento.

---

## ⚙️ Lógica de Funcionamento

### 🔄 Fluxo Principal:

```
INÍCIO
  │
  ▼
LER SENSORES (Umidade Solo, Clima, Fluxo Água)
  │
  ▼
UMIDADE DO SOLO >= UMIDADE_IDEAL?
  ├── ✅ SIM → DESLIGAR IRRIGAÇÃO → FIM
  │
  └── ❌ NÃO → CALCULAR QUANTIDADE DE ÁGUA
                    │
                    ▼
              ATIVAR IRRIGAÇÃO
                    │
                    ▼
         FLUXO_AGUA > LIMITE_FLUXO?
           ├── ✅ SIM → ⚠️ EMITIR ALERTA
           │           DESLIGAR IRRIGAÇÃO → FIM
           │
           └── ❌ NÃO → ATINGIU UMIDADE IDEAL?
                           ├── ✅ SIM → DESLIGAR IRRIGAÇÃO → FIM
                           └── ❌ NÃO → VOLTAR AO MONITORAMENTO
```

---

## 📋 Pseudocódigo

```
INÍCIO

  // Definições iniciais
  DEFINIR UMIDADE_IDEAL  = 60
  DEFINIR LIMITE_FLUXO   = 100

  // Loop contínuo de monitoramento
  ENQUANTO SISTEMA_ATIVO FAÇA

    LER UMIDADE_SOLO
    LER CLIMA
    LER FLUXO_AGUA

    SE UMIDADE_SOLO >= UMIDADE_IDEAL ENTÃO
      DESLIGAR_IRRIGAÇÃO()

    SENÃO
      CALCULAR QUANTIDADE_AGUA
      LIGAR_IRRIGAÇÃO()

      ENQUANTO IRRIGACAO_ATIVA FAÇA
        LER FLUXO_AGUA
        LER UMIDADE_SOLO

        SE FLUXO_AGUA > LIMITE_FLUXO ENTÃO
          EMITIR_ALERTA("Possível desperdício ou vazamento")
          DESLIGAR_IRRIGAÇÃO()
          PARAR
        FIMSE

      FIMENQUANTO
    FIMSE

  FIMENQUANTO

FIM
```

---

## 🧠 Regras de Negócio

| Variável | Valor | Descrição |
|---|---|---|
| `UMIDADE_IDEAL` | 60 | Nível mínimo de umidade aceitável no solo |
| `LIMITE_FLUXO` | 100 | Fluxo máximo de água antes de acionar alerta |

| Condição | Ação do Sistema |
|---|---|
| Umidade ≥ Ideal | ✅ Não irriga — solo já está úmido o suficiente |
| Umidade < Ideal | 💧 Calcula quantidade e ativa irrigação |
| Fluxo > Limite | ⚠️ Alerta de vazamento e desliga irrigação |
| Umidade ideal atingida | ✅ Desliga irrigação automaticamente |

---

## 🛠️ Conceitos Aplicados

```
✅ Estruturas de repetição (ENQUANTO / loop contínuo)
✅ Estruturas de decisão (SE / SENÃO / FIMSE)
✅ Variáveis de controle e constantes
✅ Funções de ação (LIGAR, DESLIGAR, EMITIR_ALERTA)
✅ Leitura de sensores (entrada de dados)
✅ Fluxograma com decisões múltiplas
✅ Lógica de interrupção (PARAR)
```

---

## 📁 Entregas do Projeto

```
📁 projeto-engenharia-de-solucoes-logicas/
├── 📄 pseudocodigo_irrigacao.txt    # Lógica em pseudocódigo
├── 🖼️ fluxograma_irrigacao.pdf      # Fluxograma desenhado
└── 📄 README.md                     # Documentação
```

---

## 💡 Aplicação Real

Este sistema simula o comportamento de **controladores agrícolas reais** usados em:
- Estufas automatizadas
- Plantações de precisão
- Sistemas de jardim inteligente (IoT)

A lógica desenvolvida aqui é a **base algorítmica** de sistemas embarcados que rodam em microcontroladores como Arduino e Raspberry Pi.

---

## 👨‍💻 Autor

<div align="center">

**Guilherme Henrique Souza Gonçalves**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gui995)

[⬆️ Voltar ao Portfólio](https://github.com/gui995/portfolio-guilherme-henrique-souza-goncalves)

</div>
