# Sistema de Simulação e Análise de Atendimento 📊🤖

Este projeto foi desenvolvido como parte do ecossistema acadêmico da **Universidade Federal de Viçosa (UFV)**. O objetivo principal é analisar/simular o fluxo de atendimento ao cliente, otimizando processos e identificando gargalos operacionais.

## 🎯 O Problema de Negócio
Em sistemas de atendimento, a gestão eficiente de filas e o tempo de resposta são críticos para a satisfação do cliente. Este projeto resolve o problema de atendimentos bancários que precisam lidar com indivíduos que possuem prioridade (idosos e pessoas com algum tipo de deficiência) e o tempo de espera das demais pessoas, buscando atender a todos com o máximo de justiça e agilidade.

## 🛠️ Tecnologias e Conceitos Utilizados
*   **Linguagem:** Python 3
*   **Conceitos de Ciência de Dados:** Estrutura de dados eficientes (Filas de Prioridade), modelagem de processos e análise estatística descritiva.

## 📂 Estrutura do Repositório
*   `src/atendimento.py`: Script principal contendo a lógica do sistema e algoritmos de atendimento.
*   `docs/relatorio.pdf`: Relatório acadêmico detalhado com a fundamentação teórica, métricas de avaliação e conclusões.
*   `docs/testes.pdf`: Casos de teste utilizados para garantir a resiliência e a corretude do código.

## 📈 Resultados Obtidos
*   Conseguimos simular/analisar o comportamento de uma fila bancária em diversos cenários diferentes, levando em consideração a prioridade de alguns indivíduos e o tempo de espera.
*   O algoritmo tratou com sucesso exceções de dados inválidos durante os testes de estresse.

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/PeuLucas77/sistema-simulacao-atendimento.git
2. Acesse a pasta do projeto:
   cd cd sistema-simulacao-atendimento
3. Execute o script de atendimento:
   python src/atendimento.py
