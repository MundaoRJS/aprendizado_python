class Requisição:
    def __init__(self):
        self.verificando_requisicao= input('Possue nome social S/N')
        if self.verificando_requisicao == 's':
             self.nomesocial = input('Digite aqui seu nome Social completo: ').strip()
             self.nome = input('Digite aqui seu nome completo: ').strip()
        else:
            self.nome = input('Digite aqui seu nome completo: ').strip()
        self.curso = ""
        self.telefone= ""
        self.cidade= ""
        self.matricula = ""
        self.requisição =""
        self.justificativa = ""
        self.result =""
        self.cancelamento =""
        self.usuario = ""
        self.email = ""
        self.nomesocial=""

    #Coleta de Dados do aluno Requerente
    def dados_do_requernte(self):
        self.curso = input("Curso: ").strip()
        self.matricula = input('NÚMERO DE MATRÍCULA: ').strip()
        self.telefone = input('telefone: ').strip()
        self.cidade = input('Ciade: ').strip()
        self.email = input('EMAIL: ').strip()
        self.requisição = request
        
   # Análise do requerimento solicitado
    def verify_application(self):
        if self.requisição == "Atualização de dados pessoais" or self.requisição == "Declaração"or self.requisição == "certidão de tempo de aluno" or self.requisição == "Portador de diploma" or self.requisição == "Reabertura de matrícula" or self.requisição == 'Reintegração'or self.requisição == "Renovação de Matrícula":
            self.result = self.requisição
            print()
            print (self.result)
            print()
            print('*'*60)
            print()
            print('Analizaremos o seu pedido e dentro de 48h entraremos em contato')
            print()   
        
        elif self.requisição == "justificativa de falta":
           print('='*60)
           print()
           print('Justificativa de falta aceita. Vamos remover sua falta do sistema')
           print()
           self.justificativa = input('Justifique  a sua desistência do curso :\n').strip()
           print()
        
        elif self.requisição == "cancelamento de curso":
            self.cancelamento = {
                'Aluno': self.nome,
                'Nº matrícula':self.matricula,
                'Curso':self.curso,
                'CPF':self.cpf                
            }
            print()
            self.justificativa = input('Justifique  a sua desistência do curso :\n').strip()
            print()
            
            print(f'matrícula cancelada.\n Seu Cancelamento de matrícula no curso de {self.curso} foi bem sucedido')
            print(self.cancelamento)
            
        elif self.requisição == 'Colação de Grau':
            escolha = input('Gabinete ou Solenidae pública?')
            
            print('*'*60)
            print('Analizaremos sua requisição e logo mais entraremos em contato')
            print()
            
        elif self.requisição == " Trancamento":
            self.trancamento = {
                'Aluno': self.nome,
                'Nº matrícula':self.matricula,
                'Curso':self.curso,
                'CPF':self.cpf
            }
            print(f'Curso trancado.\n Seu Trancamento de Curso {self.curso} foi bem sucedido\n voce possui um período de 2 anos com o curso trancado, se depois desses 2 anos você não voltar a realizar alguma disciplina sua matrícula no curso de {self.curso} será cancelada')
            print(self.trancamento)
            
        elif self.requisição == "Diploma/Certifcado":
             print('\n*'*60)
             print('Favor enviar para o email da instituição a digitalização dos seguinetes documentos\nCertidão de Nascimento\nQuitação Eleitoral\nCarteira de Reservista\nHistórico escolar\nNada consta da Biblioteca\n RG e CPF ')
             print()
             print('*'*60)
             print('após o recebimeto de todos os documetnos,o documeto estará pronto daqui 30 dias úteis contados apartir do dia da solicitação.\nCaso o requerente não for retiarar o Diploma/Certificado depois do prazo de 30 dias o mesmo ficará arquivado na CRDE da Instituição')
       
        elif  self.requisição == 'Guia de Transferência' or self.requisição == 'Histórico Escolar' or self.requisição == 'Reintegração' :
         self.result = {
                'Aluno': self.nome,
                'Nº matrícula':self.matricula,
                'Curso':self.curso,
                'telefone':self.telefone                
            }
         print(self.result,'logo entraremos em contato , ou por telefone ou email')
       
        elif self.requisição == 'Inclusão/Exclusão de nome social':
            if self.verificando_requisicao == 's':
                print ('Você deseja excluir seu NOme social')
            else :
                self.nomesocial = input('Digite aqui seu nome Social completo: ').strip()
                print('\n Nome Social adicionado')
        
        elif self.requisição == 'Equivalência de Disciplina' or self.requisição == 'Exame de Proeficiência' or self.requisição == 'Ementa de Disciplina':
            disciplina = input('Qual disciplina deseja fazer o processo: ').strip()
            print('\n',disciplina)
            print('Seu pedido foi gravado logo mais entraremos em contato ')
        
        elif self.requisição == 'Licença Matrenidade':
            self.result = input('Solicita atendimento domiciliar? s/n')
            if self.result == 's':
                print('seu Requerimento foi solicitado, entraremos em contato para fazer-mos o agendamento ')
            else:
                print('Requerimento foi solicitado aguarde o retorno para confirmação')
        
        elif self.requisição == 'Matrícula em disciplinas':
            self.result = input('qual(ais) disciplina(as) deseja se matricular?')
            print('Veremos se ha turma(s) disponível(eis) para as disciplinas solicitadas, e faremos a sua matrícula nela(s)')
            print()
            print('Caso não haja a possibilidade de fazer a troca , entraremos em contato, pesso que fique de olho no SIGAA')
        
        elif self.requisição == 'Mudança':
            self.result = input('qual(ais) disciplina(as) deseja efetuar a troca?')
            print('Veremos se ha turma(s) disponível(eis) para a(s) disciplina(s) solicitada(s), e efetuaremos a troca')
            print()
            print('Caso não haja a possibilidade de fazer a troca , entraremos em contato, pesso que fique de olho no SIGAA')
        
        elif self.requisição == 'Transferência':
            print('Por favor')
            self.result= input('Qual o tipo de transferência interna ou  externa?')
            if self.result == 'interna':
                print('Por Compareça na CRE para assinar os papeis')
            else:
                print ('Precisamos dos seguintes documentos: RG,CPF(do pai e da mãe se for de menor),Histórico escolar,comprovante de residência e duas fotos 3/4')        
        
        elif self.requisição == 'Outros':
            self.result = input('Digite aqui qual o tipo de requerimento que você precisa ')
            self.justificativa = ('Justifique :')
            print('Seu requrimento será anotado e logo entraremos em contato')
            
        elif self.requisição == 'Matrícula Vínculo Institucional':
            print('Precisamos dos seguintes documentos: RG,CPF(do pai e da mãe se for de menor),Histórico escolar,comprovante de residência e duas fotos 3/4')
            print('Logo entraremos em contato')
         
        elif self.requisição == 'Revisão de Avaliação' or self.requisição == 'Chamada de Prova' or self.requisição == 'Portador de diploma':
             print('ok')
             self.result = input('Nos informe a disciplina')
             self.justificativa = ('Justifique :')
            
        else:
            
            print('Requerimento não encontrado')    
            
            
          
