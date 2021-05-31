class Dados:
    nome: None
    sessao: None
    evento: None
    tipo_ingresso: None

    def dados(self, nome, evento, sessao, tipo_ingresso):
        self.nome = nome
        self.sessao = sessao

        self.evento = evento
        self.tipo_ingresso = tipo_ingresso
