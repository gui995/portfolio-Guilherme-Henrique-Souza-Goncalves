
# 🐍 Conversor de Algoritmos: Do Pseudocódigo ao Python

![Python Version](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Environment](https://img.shields.io/badge/Ambiente-Google%20Colab-orange?logo=googlecolab&logoColor=white)

## 📝 Visão Geral do Projeto

Este repositório reúne uma série de scripts desenvolvidos em Python que ilustram a transposição prática de pseudocódigos clássicos para código executável de alto nível. O objetivo principal é consolidar a aplicação de desvios condicionais, loops de repetição e o tratamento rigoroso de tipos primitivos em cenários do mundo real.

A suíte de testes contempla quatro módulos analíticos:
* **Módulo de Vendas**: Motor de faturamento que valida dados de estoque e aplica regras de descontos progressivos (escalonados em 5% e 10%).
* **Módulo Meteorológico**: Monitor de oscilações térmicas semanais com cálculo de médias aritméticas e disparo de sinalizadores de emergência para extremos climáticos.
* **Módulo de Desempenho Acadêmico**: Console de avaliação de turmas que calcula médias e categoriza estudantes entre aprovação direta, exame de recuperação ou retenção.
* **Módulo de Projeção de Ativos**: Calculadora de juros sobre investimentos que aceita depósitos mensais flutuantes e valida o atingimento de metas financeiras.

## 🚀 Arquitetura de Código e Regras Aplicadas

As soluções contornam particularidades da linguagem através de boas práticas de desenvolvimento:
* **Tratamento de Input (Casting)**: Conversão forçada das entradas do usuário para `float` ou `int`, blindando o sistema contra erros de tipos nas operações matemáticas.
* **Controle de Laço Inclusivo**: Emprego estratégico da estrutura `range(1, limite + 1)` para espelhar de forma fiel o comportamento dos laços `PARA` tradicionais.
* **Flags de Estado**: Uso de variáveis booleanas para monitoramento contínuo de eventos críticos, como riscos climáticos ou metas de capital acumulado (alvo de R$ 10k).

## 🔧 Como Executar a Aplicação

1. Baixe o script principal `projeto-traduzindo-logica-para-python.py` ou abra o notebook diretamente via Google Colab.
2. Invoque a função que deseja avaliar diretamente no escopo de execução:
   - `processar_vendas()`
   - `analisar_clima()`
   - `sistema_notas_turma()`
   - `simulador_poupanca()`
3. Responda aos prompts do terminal para interagir com os fluxos do algoritmo.

## 🧠 Análise Crítica e Aprendizados

O processo de migração de lógica abstrata para Python destacou duas características fundamentais da linguagem:
* **Natureza das Strings**: Por padrão, o método `input()` lê dados como texto. Sem o devido isolamento numérico, operações aritméticas quebram ou geram concatenações inesperadas.
* **Comportamento do Indexador**: O intervalo final do `range` é excludente por padrão na engenharia do Python. Dominar essa regra foi crucial para evitar erros de contagem de tempo (erros de tipo *off-by-one*).

---
*Repositório acadêmico voltado ao estudo de Algoritmos e Estruturas de Dados.*
