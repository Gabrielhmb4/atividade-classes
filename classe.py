class Contato:  
  def __init__(self, nome, email):
    self.nome = nome 
    self.email = email 

    def atualizar_nome(self,novo_nome):
      self.nome = novo_nome 

    def atualizar_email(self, novo_email):
        self.email = novo_email 

    def to_adict(self): 
      return {"nome": self.nome, "email": self.email} 


    delf __str__(self):
      return f"{self.nome} ({self.email})"
