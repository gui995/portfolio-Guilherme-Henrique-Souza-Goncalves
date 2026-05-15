projeto-auditoria-financeira/README.md
<div align="center">

# 🛡️ Sistema de Auditoria de Dados de Vendas

**Detecção inteligente de anomalias financeiras em tempo real**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-28a745?style=for-the-badge)
![Faculdade](https://img.shields.io/badge/Projeto-Acadêmico-orange?style=for-the-badge)

</div>

---

## 📌 Sobre o Projeto

> Sistema de monitoramento automatizado que atua como uma **camada de segurança** para fluxos financeiros de vendas, detectando anomalias e garantindo a integridade dos dados antes que causem impacto no negócio.

O algoritmo processa lotes de vendas em tempo real, calcula métricas de desempenho e aplica filtros de quarentena automáticos. Quando uma transação suspeita é detectada, o sistema **interrompe o fluxo e exige validação manual** de um gestor — com capacidade de ajuste dinâmico dos parâmetros de segurança durante a execução.

---

## ⚙️ Funcionalidades

| # | Funcionalidade | Descrição |
|---|---|---|
| 1 | 📊 **Cálculo de Média** | Processa a média aritmética de lotes de vendas para análise de volume |
| 2 | 🔒 **Filtro de Quarentena** | Bloqueia automaticamente o sistema quando a média ultrapassa o `LIMITE_SEGURANCA` |
| 3 | 🔍 **Detecção de Outliers** | Identifica valores individuais que divergem drasticamente da média |
| 4 | 🎛️ **Ajuste Dinâmico** | Permite ao gestor validar vendas e atualizar o limite global em tempo real via console |

---

## 🧠 Fluxo do Sistema

```
📥 Entrada de vendas
        ↓
📊 Cálculo da média do lote
        ↓
🔎 Média > LIMITE_SEGURANCA?
   ├── ✅ NÃO → Processamento normal
   └── ❌ SIM → 🔒 Quarentena ativada
                    ↓
              👤 Revisão do gerente
                    ↓
         ┌──────────────────────┐
         │ Aprovar → Atualiza   │
         │ limite e continua    │
         │ Rejeitar → Bloqueia  │
         └──────────────────────┘
```

---

## 🛠️ Tecnologias

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![VSCode](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white)
![Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)

</div>

**Conceitos aplicados:**
- Escopo de variáveis globais
- Estruturas condicionais avançadas
- Manipulação de tipos (`float`, `string`)
- Entrada de dados dinâmica via console
- Lógica de negócio com regras de quarentena

---

## 🚀 Como Executar

**Pré-requisito:** Python 3.x instalado → [python.org](https://python.org)

```bash
# 1. Clone o repositório
git clone https://github.com/gui995/portfolio-guilherme-henrique-souza-goncalves

# 2. Acesse a pasta do projeto
cd projeto-algoritmo-de-auditoria-de-dados

# 3. Execute o script
python projeto_algoritimo_de_alditoria_de_dados.py
```

---

## 📂 Estrutura do Projeto

```
📁 projeto-algoritmo-de-auditoria-de-dados/
├── 📄 projeto_algoritimo_de_alditoria_de_dados.py   # Script principal
└── 📄 README.md                                      # Documentação
```

---

## 👨‍💻 Autor

<div align="center">

**Guilherme Henrique Souza Gonçalves**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/seu-perfil)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gui995)

[⬆️ Voltar ao Portfólio](https://github.com/gui995/portfolio-guilherme-henrique-souza-goncalves)

</div>
