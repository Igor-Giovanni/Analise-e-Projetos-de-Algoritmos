import time
from atividade import Atividade
from testes import gerar_casos
from algoritmos import selecao_gulosa, selecao_dp

# ==========================================
# FUNÇÕES DE INTERFACE
# ==========================================
def cadastrar_atividade_manual(vetor_atividades):
    """Permite o cadastro manual via terminal e adiciona ao vetor em memória."""
    print("\n--- CADASTRO MANUAL DE ATIVIDADE ---")
    codigo = input("Código da atividade: ")
    nome = input("Nome da atividade: ")
    inicio = int(input("Horário de início (ex: 8): "))
    fim = int(input("Horário de fim (ex: 10): "))
    prioridade = int(input("Prioridade (1 a 5): "))
    participantes = int(input("Quantidade de participantes: "))

    nova_atividade = Atividade(codigo, nome, inicio, fim, prioridade, participantes)
    vetor_atividades.append(nova_atividade)
    print("Atividade cadastrada com sucesso no vetor!\n")

def exibir_atividades(vetor_atividades):
    """Percorre o vetor e imprime todos os atributos de forma legível."""
    print(f"\n--- LISTA DE ATIVIDADES ({len(vetor_atividades)} cadastradas) ---")
    for atv in vetor_atividades:
        print(f"[{atv.codigo}] {atv.nome}")
        print(f"    Horário: {atv.inicio}h às {atv.fim}h")
        print(f"    Prioridade: {atv.prioridade} | Participantes: {atv.participantes}")
        print(f"    Peso Calculado (DP): {atv.peso}\n")

def executar_e_comparar(nome_teste, vetor_atividades):
    """Executa ambas as estratégias no vetor fornecido e exibe os resultados."""
    print(f"\n{'='*50}\n{nome_teste} ({len(vetor_atividades)} Atividades)\n{'='*50}")
    
    vetor_para_guloso = vetor_atividades.copy()
    vetor_para_dp = vetor_atividades.copy()
    
    # Execução do Guloso
    inicio_guloso = time.perf_counter()
    resultado_guloso = selecao_gulosa(vetor_para_guloso)
    tempo_guloso = time.perf_counter() - inicio_guloso
    beneficio_guloso = sum(a.peso for a in resultado_guloso)
    
    # Execução da Programação Dinâmica
    inicio_dp = time.perf_counter()
    resultado_dp = selecao_dp(vetor_para_dp)
    tempo_dp = time.perf_counter() - inicio_dp
    beneficio_dp = sum(a.peso for a in resultado_dp)
    
    # Exibição dos Resultados
    print(f"[ESTRATÉGIA GULOSA]")
    print(f" -> Atividades agendadas: {len(resultado_guloso)}")
    print(f" -> Atividades selecionadas: {[a.codigo for a in resultado_guloso]}")
    print(f" -> Benefício Total: {beneficio_guloso}")
    print(f" -> Tempo de Execução: {tempo_guloso:.6f} segundos")
    
    print(f"\n[PROGRAMAÇÃO DINÂMICA]")
    print(f" -> Atividades agendadas: {len(resultado_dp)}")
    print(f" -> Atividades selecionadas: {[a.codigo for a in resultado_dp]}")
    print(f" -> Benefício Total: {beneficio_dp}")
    print(f" -> Tempo de Execução: {tempo_dp:.6f} segundos")
    
    print("\n[Veredito do Caso]")
    if len(resultado_guloso) >= len(resultado_dp):
        print(" -> O Guloso conseguiu agendar igual ou mais atividades em quantidade.")
    if beneficio_dp >= beneficio_guloso:
        print(" -> A DP conseguiu um benefício (prioridade x público) maior ou igual ao Guloso.")

# ==========================================
# BLOCO PRINCIPAL (EXECUÇÃO)
# ==========================================
if __name__ == "__main__":
    print("SISTEMA DE AGENDAMENTO DE ATIVIDADES - UFBA")
    
    # 1. MENU DE CADASTRO MANUAL
    vetor_manual = []
    print("\n[Módulo de Cadastro Manual]")
    
    while True:
        opcao = input("Deseja cadastrar uma atividade manualmente? (s/n): ").strip().lower()
        if opcao == 's':
            cadastrar_atividade_manual(vetor_manual)
        elif opcao == 'n':
            break
        else:
            print("Opção inválida. Digite 's' ou 'n'.")
    
    if len(vetor_manual) > 0:
        exibir_atividades(vetor_manual)
        executar_e_comparar("Teste Manual Personalizado", vetor_manual)
    else:
        print("\nNenhuma atividade manual cadastrada. Seguindo para os testes automáticos...")

    # 2. BATERIA DE TESTES AUTOMÁTICOS DO EDITAL
    vetor_teste_1 = gerar_casos(8)
    print("\n>>> GERANDO TESTE 1 (PEQUENO) <<<")
    exibir_atividades(vetor_teste_1) 
    executar_e_comparar("Teste 1 - Pequeno", vetor_teste_1)

    vetor_teste_2 = gerar_casos(15)
    executar_e_comparar("Teste 2 - Médio", vetor_teste_2)

    vetor_teste_3 = gerar_casos(50)
    executar_e_comparar("Teste 3 - Grande", vetor_teste_3)