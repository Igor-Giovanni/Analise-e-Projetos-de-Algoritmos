def merge_sort(vetor, chave=lambda x: x.fim):
    """
    Ordena um vetor de atividades garantindo a complexidade O(n log n).
    Utiliza o paradigma Divisão e Conquista.
    """
    # Condição de parada da recursão: um vetor de tamanho 1 já está ordenado.
    if len(vetor) > 1:
        # DIVISÃO:
        meio = len(vetor) // 2
        metade_esq = vetor[:meio]
        metade_dir = vetor[meio:]

        # Chamada recursiva para dividir até chegar em vetores unitários
        merge_sort(metade_esq, chave)
        merge_sort(metade_dir, chave)

        # CONQUISTA (Intercalação/Merge):
        i = 0 # Ponteiro para percorrer a metade esquerda
        j = 0 # Ponteiro para percorrer a metade direita
        k = 0 # Ponteiro para a posição atual no vetor original

        # Compara os elementos das duas metades e insere o menor no vetor original
        while i < len(metade_esq) and j < len(metade_dir):
            # A função 'chave' permite escolher dinamicamente por qual atributo ordenar 
            # (neste projeto, será pelo atributo '.fim' da Atividade)
            if chave(metade_esq[i]) <= chave(metade_dir[j]):
                vetor[k] = metade_esq[i]
                i += 1
            else:
                vetor[k] = metade_dir[j]
                j += 1
            k += 1

        # RESÍDUOS:
        # Se uma das metades esvaziar primeiro, copiamos o restante da outra metade.
        while i < len(metade_esq):
            vetor[k] = metade_esq[i]
            i += 1
            k += 1

        while j < len(metade_dir):
            vetor[k] = metade_dir[j]
            j += 1
            k += 1

    return vetor