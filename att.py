import random
class banco:
    def __init__(self):
        self.nome = input('Digite aqui seu nome completo: ').strip()
        self.conta = ""
        self.cpf = ""
        self.id = ""

    #Coleta de Dados do aluno Requerente
    def Agência(self):
        self.cpf = input('CPF: ').strip()      
        self.conta = input("tipo de conta: ").strip()
        
        
   # Análise do requerimento solicitado
    def Contacorrente(self):
        self.conta= {
            'nome': self.nome,
            'Cpf' : self.cpf            
        }
        self.id= random.randrange(0,2000)
        print(self.conta)
        print(f'202200254{self.id}')

usuario = banco()
usuario.Agência()
usuario.Contacorrente()
