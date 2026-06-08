import random
from atividade import Atividade

def gerar_casos(tamanho):
    """
    Gera um vetor preenchido com instâncias da classe Atividade contendo 
    horários, públicos e prioridades aleatórias para simulações de carga.
    """
    vetor_gerado = []
    for i in range(tamanho):
        inicio = random.randint(8, 18)
        duracao = random.randint(1, 4)
        
        # Instancia o objeto e apenda no vetor
        nova_atividade = Atividade(
            codigo=f"A{i+1:03d}",
            nome=f"Treinamento/Reunião {i+1}",
            inicio=inicio,
            fim=inicio + duracao,
            prioridade=random.randint(1, 3),
            participantes=random.randint(10, 100)
        )
        vetor_gerado.append(nova_atividade)
        
    return vetor_gerado