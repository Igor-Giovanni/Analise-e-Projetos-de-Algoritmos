from ordenacao import merge_sort

def selecao_gulosa(vetor_atividades):
    """
    Seleciona o maior número absoluto de atividades.
    Estratégia: Escolher as que terminam mais cedo para liberar espaço rapidamente.
    """
    if not vetor_atividades:
        return []

    # Passo 1: Copiar o vetor e ordenar pelo término.
    vetor_ordenado = vetor_atividades.copy()
    merge_sort(vetor_ordenado, chave=lambda a: a.fim) # Ordena as atividades pelo horário de término (atributo .fim) usando Merge Sort. 
                                                      # Complexidade O(n log n). 
                                                      # a chave lambda a: a.fim indica que a ordenação deve ser feita com base no atributo 'fim' de cada atividade.

    # Passo 2: A primeira atividade a terminar é sempre selecionada.
    selecionadas = [vetor_ordenado[0]]
    ultimo_fim = vetor_ordenado[0].fim

    # Passo 3: Percorrer o restante do vetor sequencialmente
    for i in range(1, len(vetor_ordenado)):
        # Se a atividade atual começa depois (ou no mesmo horário) que a anterior terminou,
        # não há conflito. Seleciona ela.
        if vetor_ordenado[i].inicio >= ultimo_fim:
            selecionadas.append(vetor_ordenado[i])
            ultimo_fim = vetor_ordenado[i].fim # Atualiza o referencial de término

    return selecionadas

def busca_binaria_conflito(vetor, indice):
    """
    Para a atividade no índice atual, busca a atividade MAIS RECENTE que terminou
    antes desta começar. Isso é fundamental para a DP não ter complexidade O(n^2).
    """
    inicio = 0
    fim = indice - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        # Verifica se a atividade do 'meio' termina antes da atividade atual começar
        if vetor[meio].fim <= vetor[indice].inicio:
            # Se a próxima atividade também for compatível, continuamos buscando mais à direita 
            # para pegar a mais próxima possível.
            if vetor[meio + 1].fim <= vetor[indice].inicio:
                inicio = meio + 1
            else:
                return meio # Encontramos a atividade compatível ideal
        else:
            # Há conflito, então devemos buscar em atividades que terminaram mais cedo (à esquerda)
            fim = meio - 1
            
    return -1 # Retorna -1 se todas as atividades anteriores conflitarem

def selecao_dp(vetor_atividades):
    """
    Maximiza o peso total (prioridade x participantes) selecionado.
    Garante a solução ótima onde a abordagem Gulosa falha.
    """
    if not vetor_atividades:
        return []

    n = len(vetor_atividades)
    vetor = vetor_atividades.copy()
    merge_sort(vetor, chave=lambda a: a.fim)

    # Vetor DP: dp[i] armazena o "lucro" máximo que podemos obter analisando até o índice i.
    dp = [0] * n
    dp[0] = vetor[0].peso # O caso base é o peso da primeira atividade

    # Fase 1: Preencher a tabela DP resolvendo subproblemas
    for i in range(1, n):
        peso_incluindo = vetor[i].peso
        
        # Busca a atividade anterior compatível para somar os lucros
        l = busca_binaria_conflito(vetor, i)
        if l != -1:
            peso_incluindo += dp[l]
        
        # A decisão ótima: O que vale mais? O lucro INCLUINDO esta atividade ou IGNORANDO-A (mantendo o lucro anterior)?
        dp[i] = max(peso_incluindo, dp[i-1])

    # Fase 2: Backtracking (Recuperar as atividades que formaram o lucro ótimo)
    selecionadas = []
    i = n - 1
    while i >= 0:
        l = busca_binaria_conflito(vetor, i)
        peso_incluindo = vetor[i].peso + (dp[l] if l != -1 else 0)
        
        # Se o lucro incluindo for maior ou igual ao lucro ignorando, significa que a atividade i 
        # fez parte da solução ótima. Nós a adicionamos e saltamos para a última atividade compatível (l).
        if i == 0 or peso_incluindo >= dp[i-1]:
            selecionadas.append(vetor[i])
            i = l
        else:
            # A atividade não foi usada, recuamos apenas 1 índice
            i -= 1

    # Invertemos o vetor porque o backtracking recolheu as atividades do fim para o começo
    selecionadas.reverse()
    return selecionadas