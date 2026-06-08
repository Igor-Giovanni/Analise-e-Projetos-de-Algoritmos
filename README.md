# Projeto Integrador - Sistema de Agendamento de Atividades

**Instituição:** Universidade Federal da Bahia (UFBA)
**Disciplina:** Analise e Projetos de Algoritmos
**Professor(a):** Prof. Dra. Larissa Barbosa Leôncio Pinheiro  
**Autor:** Igor Giovanni Gomes Silva  

---

## Visão Geral do Projeto

Este projeto consiste no desenvolvimento de um sistema computacional capaz de selecionar o maior número possível de atividades (treinamentos, palestras e reuniões) em uma agenda que possui conflitos de horário. 

O sistema implementa, analisa e compara duas abordagens algorítmicas clássicas para a resolução de problemas de otimização: o **Algoritmo Guloso** (focado em maximizar a quantidade absoluta de atividades) e a **Programação Dinâmica** (focada em maximizar o benefício/peso total das atividades selecionadas com base na prioridade e na quantidade de participantes).

---

## Cumprimento dos Objetivos (Edital)

O projeto foi desenvolvido em **Python** e atende a todos os critérios obrigatórios estabelecidos no Estudo de Caso:

- [x] **Cadastro e Estruturação de Atividades:** Cada atividade possui Código, Nome, Horário de Início, Horário de Fim, Prioridade e Quantidade de Participantes.
- [x] **Algoritmo de Ordenação:** Implementação nativa e obrigatória do **Merge Sort** para a ordenação dos vetores de atividades.
- [x] **Algoritmo Guloso:** Seleção clássica de atividades visando evitar sobreposição e maximizar a quantidade.
- [x] **Programação Dinâmica (DP):** Implementação adicional utilizando DP para complementar a solução gulosa, maximizando o benefício total (Prioridade $\times$ Participantes).
- [x] **Comparação e Análise de Desempenho:** O sistema afere o tempo de execução e a qualidade da solução entre as duas abordagens.
- [x] **Bateria de Testes:** Execução automatizada validando Teste 1 Pequeno (5 a 8), Teste 2 Médio (10 a 20) e Teste 3 Maior (+30 atividades).

---

## Arquitetura e Modularização

Visando as melhores práticas de Engenharia de Software, o sistema foi modularizado em 5 arquivos distintos para garantir clareza, manutenibilidade e separação de responsabilidades. Todas as coleções de dados são tratadas estritamente como **vetores** em memória, garantindo acesso em tempo constante `O(1)` para viabilizar as buscas binárias.

1. **`atividade.py`**: Contém a classe de domínio `Atividade`. Centraliza a modelagem dos dados e o cálculo do benefício (peso) utilizado pela Programação Dinâmica.
2. **`ordenacao.py`**: Isola a implementação do algoritmo `merge_sort`. A função recebe uma função `lambda` como chave, permitindo ordenar os vetores dinamicamente pelo horário de término.
3. **`algoritmos.py`**: O núcleo lógico do sistema. Contém a heurística `selecao_gulosa`, a `busca_binaria_conflito` e o núcleo de `selecao_dp`.
4. **`testes.py`**: Gerador de massas de dados. Responsável por instanciar os vetores de atividades aleatórias (com horários lógicos) para simular cenários de sobreposição.
5. **`main.py`**: O arquivo orquestrador. Implementa a interface de linha de comando (CLI), o menu para cadastro manual de atividades, o benchmark (medição de tempo com `time.perf_counter()`) e exibe o veredito das comparações.

---

## Análise de Complexidade

| Algoritmo | Complexidade de Tempo | Complexidade de Espaço |
| :--- | :--- | :--- |
| **Merge Sort** | `O(n log n)` | `O(n)` (Devido à divisão dos vetores) |
| **Busca Binária** | `O(log n)` | `O(1)` |
| **Algoritmo Guloso** | `O(n log n)` | `O(n)` (Cópia do vetor ordenado) |
| **Programação Dinâmica**| `O(n log n)` | `O(n)` (Tabela DP de memoização) |

*Nota: As resoluções de seleção possuem complexidade iterativa de `O(n)`, contudo, são dominadas assintoticamente pelo passo obrigatório de ordenação inicial `O(n log n)`.*

---

## Como Executar o Projeto

**Pré-requisitos:** Python 3.x instalado na máquina. Nenhuma biblioteca externa é necessária.

1. Clone o repositório ou baixe os arquivos em uma única pasta.
2. Abra o terminal de comando (ou bash) no diretório do projeto.
3. Execute o arquivo principal com o comando:
   ```bash
   python main.py
4. Siga as instruções no terminal. Você poderá optar por cadastrar atividades manualmente para testar o comportamento dos algoritmos ou avançar diretamente para a bateria de testes automáticos exigida pelo edital.