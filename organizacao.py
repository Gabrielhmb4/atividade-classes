from classe import Contato

class ContatoRepo:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato: Contato):
        self.contatos.append(contato)

    def editar(self, indice, novo_nome=None, novo_email=None):
        if 0 <= indice < len(self.contatos):
            if novo_nome:
                self.contatos[indice].atualizar_nome(novo_nome)
            if novo_email:
                self.contatos[indice].atualizar_email(novo_email)

    def remover(self, indice):
        if 0 <= indice < len(self.contatos):
            self.contatos.pop(indice)

    def listar(self):
        return [str(c) for c in self.contatos]
