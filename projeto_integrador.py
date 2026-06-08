import time
import random

# ==========================================
# 1. CLASSE DE DADOS
# ==========================================
class Atividade:
    def __init__(self, codigo, nome, inicio, fim, prioridade, participantes):
        self.codigo = codigo
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
        self.prioridade = prioridade
        self.participantes = participantes
        # Peso para a DP: maximizar o público priorizado
        self.peso = participantes * prioridade 

    def __repr__(self):
        return f"[{self.codigo}] {self.nome} ({self.inicio}h-{self.fim}h) | Peso: {self.peso}"

# ==========================================
# 2. ALGORITMO DE ORDENAÇÃO: MERGE SORT
# ==========================================
def merge_sort(vetor, chave=lambda x: x.fim):
    """
    Ordena um vetor de atividades garantindo a complexidade O(n log n).
    O parâmetro 'chave' permite definir por qual atributo ordenar.
    """
    if len(vetor) > 1:
        meio = len(vetor) // 2
        metade_esq = vetor[:meio]
        metade_dir = vetor[meio:]

        merge_sort(metade_esq, chave)
        merge_sort(metade_dir, chave)

        i = j = k = 0

        # Intercalação
        while i < len(metade_esq) and j < len(metade_dir):
            if chave(metade_esq[i]) <= chave(metade_dir[j]):
                vetor[k] = metade_esq[i]
                i += 1
            else:
                vetor[k] = metade_dir[j]
                j += 1
            k += 1

        # Resíduos
        while i < len(metade_esq):
            vetor[k] = metade_esq[i]
            i += 1
            k += 1

        while j < len(metade_dir):
            vetor[k] = metade_dir[j]
            j += 1
            k += 1

    return vetor

# ==========================================
# 3. ALGORITMO GULOSO (MAIOR QUANTIDADE)
# ==========================================
def selecao_gulosa(vetor_atividades):
    """
    Seleciona o maior número de atividades sem conflito.
    Critério: Escolher sempre a atividade que termina mais cedo.
    """
    if not vetor_atividades:
        return []

    # Ordena pelo horário de término usando o Merge Sort obrigatório
    vetor_ordenado = vetor_atividades.copy()
    merge_sort(vetor_ordenado, chave=lambda a: a.fim)

    selecionadas = [vetor_ordenado[0]]
    ultimo_fim = vetor_ordenado[0].fim

    for i in range(1, len(vetor_ordenado)):
        if vetor_ordenado[i].inicio >= ultimo_fim:
            selecionadas.append(vetor_ordenado[i])
            ultimo_fim = vetor_ordenado[i].fim

    return selecionadas

# ==========================================
# 4. PROGRAMAÇÃO DINÂMICA (MAIOR BENEFÍCIO)
# ==========================================
def busca_binaria_conflito(vetor, indice):
    """
    Encontra o índice da última atividade que não conflita com a atividade atual.
    Retorna -1 se não houver nenhuma compatível.
    """
    inicio = 0
    fim = indice - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vetor[meio].fim <= vetor[indice].inicio:
            if vetor[meio + 1].fim <= vetor[indice].inicio:
                inicio = meio + 1
            else:
                return meio
        else:
            fim = meio - 1
    return -1

def selecao_dp(vetor_atividades):
    """
    Maximiza o benefício total (peso) usando Programação Dinâmica.
    """
    if not vetor_atividades:
        return []

    n = len(vetor_atividades)
    vetor = vetor_atividades.copy()
    merge_sort(vetor, chave=lambda a: a.fim)

    # dp[i] armazena o lucro máximo até a atividade i
    dp = [0] * n
    dp[0] = vetor[0].peso

    for i in range(1, n):
        peso_incluindo = vetor[i].peso
        l = busca_binaria_conflito(vetor, i)
        if l != -1:
            peso_incluindo += dp[l]
        
        dp[i] = max(peso_incluindo, dp[i-1])

    # Reconstrução da solução (Backtracking na tabela DP)
    selecionadas = []
    i = n - 1
    while i >= 0:
        l = busca_binaria_conflito(vetor, i)
        peso_incluindo = vetor[i].peso + (dp[l] if l != -1 else 0)
        
        if i == 0 or peso_incluindo >= dp[i-1]:
            selecionadas.append(vetor[i])
            i = l
        else:
            i -= 1

    selecionadas.reverse()
    return selecionadas

# ==========================================
# 5. TESTES E BENCHMARK
# ==========================================
def gerar_casos(tamanho):
    """Gera um vetor de atividades aleatórias para simular entradas."""
    atividades = []
    for i in range(tamanho):
        inicio = random.randint(8, 18)
        duracao = random.randint(1, 4)
        atividades.append(Atividade(
            codigo=f"A{i+1:03d}",
            nome=f"Treinamento/Reunião {i+1}",
            inicio=inicio,
            fim=inicio + duracao,
            prioridade=random.randint(1, 3),
            participantes=random.randint(10, 100)
        ))
    return atividades

def cadastrar_atividade_manual(vetor_atividades):
    """Permite o cadastro manual via terminal e adiciona ao vetor."""
    print("\n--- CADASTRO MANUAL DE ATIVIDADE ---")
    codigo = input("Código da atividade: ")
    nome = input("Nome da atividade: ")
    inicio = int(input("Horário de início (ex: 8): "))
    fim = int(input("Horário de fim (ex: 10): "))
    prioridade = int(input("Prioridade (1 a 5): "))
    participantes = int(input("Quantidade de participantes: "))

    # Instancia o objeto e anexa ao vetor
    nova_atividade = Atividade(codigo, nome, inicio, fim, prioridade, participantes)
    vetor_atividades.append(nova_atividade)
    print("Atividade cadastrada com sucesso no vetor!\n")

def exibir_atividades(vetor_atividades):
    """Percorre o vetor e imprime todos os atributos formatados."""
    print(f"\n--- LISTA DE ATIVIDADES ({len(vetor_atividades)} cadastradas) ---")
    for atv in vetor_atividades:
        # Acessando cada atributo 
        print(f"[{atv.codigo}] {atv.nome}")
        print(f"    Horário: {atv.inicio}h às {atv.fim}h")
        print(f"    Prioridade: {atv.prioridade} | Participantes: {atv.participantes}")
        print(f"    Peso Calculado (DP): {atv.peso}\n")

def executar_e_comparar(nome_teste, vetor_atividades):
    """
    Recebe um nome para o teste e um vetor de atividades JÁ PRONTO.
    Executa ambas as estratégias e exibe os resultados comparativos.
    """
    print(f"\n{'='*50}\n{nome_teste} ({len(vetor_atividades)} Atividades)\n{'='*50}")
    
    # Criamos cópias do vetor original para não alterar a ordem inicial
    vetor_para_guloso = vetor_atividades.copy()
    vetor_para_dp = vetor_atividades.copy()
    
    # ==========================
    # Algoritmo Guloso
    # ==========================
    inicio_guloso = time.perf_counter()
    resultado_guloso = selecao_gulosa(vetor_para_guloso)
    tempo_guloso = time.perf_counter() - inicio_guloso
    beneficio_guloso = sum(a.peso for a in resultado_guloso)
    
    # ==========================
    # Programação Dinâmica
    # ==========================
    inicio_dp = time.perf_counter()
    resultado_dp = selecao_dp(vetor_para_dp)
    tempo_dp = time.perf_counter() - inicio_dp
    beneficio_dp = sum(a.peso for a in resultado_dp)
    
    # ==========================
    # Exibição dos Resultados
    # ==========================
    print(f"[ESTRATÉGIA GULOSA]")
    print(f" -> Atividades agendadas: {len(resultado_guloso)}")
    print(f" -> Atividades disponíveis: {[a.codigo for a in vetor_atividades]}")
    print(f" -> Atividades selecionadas: {[a.codigo for a in resultado_guloso]}")
    print(f" -> Benefício Total: {beneficio_guloso}")
    print(f" -> Tempo de Execução: {tempo_guloso:.6f} segundos")
    
    print(f"\n[PROGRAMAÇÃO DINÂMICA]")
    print(f" -> Atividades agendadas: {len(resultado_dp)}")
    print(f" -> Atividades disponíveis: {[a.codigo for a in vetor_atividades]}")
    print(f" -> Atividades selecionadas: {[a.codigo for a in resultado_dp]}")
    print(f" -> Benefício Total: {beneficio_dp}")
    print(f" -> Tempo de Execução: {tempo_dp:.6f} segundos")
    
    print("\n[Veredito do Caso]")
    if len(resultado_guloso) >= len(resultado_dp):
        print(" -> O Guloso conseguiu agendar igual ou mais atividades em quantidade.")
    if beneficio_dp >= beneficio_guloso:
        print(" -> A DP conseguiu um benefício (prioridade x público) maior ou igual ao Guloso.")

if __name__ == "__main__":
    print("SISTEMA DE AGENDAMENTO DE ATIVIDADES - UFBA")
    
    # ==========================================
    # MÓDULO DE CADASTRO MANUAL
    # ==========================================
    vetor_manual = []
    print("\n[Módulo de Cadastro Manual]")
    
    while True:
        opcao = input("Deseja cadastrar uma atividade manualmente? (s/n): ").strip().lower()
        if opcao == 's':
            cadastrar_atividade_manual(vetor_manual)
        elif opcao == 'n':
            break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")
    
    # Se o usuário cadastrou pelo menos uma atividade, o sistema analisa esse vetor
    if len(vetor_manual) > 0:
        exibir_atividades(vetor_manual)
        executar_e_comparar("Teste Manual Personalizado", vetor_manual)
    else:
        print("\nNenhuma atividade manual cadastrada. Seguindo para os testes automáticos...")

    # ==========================================
    # MÓDULO DE TESTES AUTOMÁTICOS (EDITAL)
    # ==========================================
    # Teste 1 (Pequeno)
    vetor_teste_1 = gerar_casos(8)
    print("\n>>> GERANDO TESTE 1 (PEQUENO) <<<")
    exibir_atividades(vetor_teste_1) 
    executar_e_comparar("Teste 1 - Pequeno", vetor_teste_1)

    # Teste 2 (Médio)
    vetor_teste_2 = gerar_casos(15)
    executar_e_comparar("Teste 2 - Médio", vetor_teste_2)

    # Teste 3 (Grande)
    vetor_teste_3 = gerar_casos(50)
    executar_e_comparar("Teste 3 - Grande", vetor_teste_3)