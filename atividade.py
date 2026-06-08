class Atividade:
    """
    Representa uma entidade de Atividade a ser agendada.
    Essa classe agrupa todos os atributos exigidos pelo edital.
    """
    def __init__(self, codigo, nome, inicio, fim, prioridade, participantes):
        self.codigo = codigo
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
        self.prioridade = prioridade
        self.participantes = participantes
        
        # O peso é o critério de valor para a Programação Dinâmica.
        # Multiplicamos o público pela prioridade para obter o "benefício" real da atividade.
        self.peso = participantes * prioridade 

    def __repr__(self):
        # O método __repr__ define como o objeto é exibido quando impresso.
        return f"[{self.codigo}] {self.nome} ({self.inicio}h-{self.fim}h) | Peso: {self.peso}"