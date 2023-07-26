class Requisição:
    def __init__(self):
        verificando_requisicao= input('Possue nome social S/N')
        if verificando_requisicao == 's':
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
    def dados_do_requerente(self):
        self.curso = input("Curso: ").strip()
        self.matricula = input('NÚMERO DE MATRÍCULA: ').strip()
        self.telefone = input('telefone: ').strip()
        self.cidade = input('Ciade: ').strip()
        self.email = input('EMAIL: ').strip()
        self.requisição = request
        
   # Análise do requerimento solicitado
    def verify_requests(self):
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
           print()
           self.justificativa = input('Justifique  seu motivo de falta.Depois no final indique a(s) matéria(s) e o(s) horário(s):\n').strip()
           print()
           print('Iremos analisar a sua justificativa de falta.\nCaso seja aceita faremos a remoção da falta do sistema , do contrário entraremos em contato para explicar a situação.\nSe o senhor(a) tiver uma declaração favor entregar na CRE.')
        
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
            if verificando_requisicao == 's':
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
            
            
          
print("="*60)

#Tipos de requirementos 

req1 ='Atualização de dados pessoais' 
req2 ='cancelamento de curso'
req3 ='certidão de tempo de aluno'
req4 ='Colação de Grau'
req5 ='Declaração' 
req6 ='Diploma/Certifcado'
req7 = 'Ementa de Disciplina'
req8 ='Inclusão/Exclusão de nome social'
req9 ='Equivalência de Disciplina' 
req10='Exame de Proeficiência'
req11= 'Guia de Transferência'
req12='Histórico Escolar'
req13='justificativa de falta' 
req14='Licença Matrenidade' 
req15= 'Matrícula em disciplinas'
req16='Mudança'
req17='Portador de diploma' 
req18='Reabertura de matrícula'
req19= 'Reintegração'
req20='Renovação de Matrícula'
req21='Revisão de Avaliação' 
req22='Chamada de Prova'
req23= 'Trancamento'
req24='Transferência'
req25='Outros'
req26='Matrícula Vínculo Institucional'
 

#Realizando escolha do requerimento
       
usuario= str(input ('qual tipo de requerimento você deseja solicitar :\n1 =Atualização de dados pessoais\n2 =cancelamento de curso \n3 =certidão de tempo de aluno\n4 =Colação de Grau\n5=Declaração \n6 =Diploma/Certifcado\n7 = Ementa de Disciplina\n8 =Inclusão/Exclusãode nome social\n9 =Equivalência de Disciplina\n10=Exame de Proeficiência\n11= Guia de Transferência\n12=Histórico Escolar\n13=justificativa de falta \n14=Licença Matrenidade\n15= Matrícula em disciplinas \n16=Mudança\n17=Portador de diploma\n18=Reabertura de matrícula\n19= Reintegração\n20=Renovação de Matrícula\n21=Revisão de Avaliação\n22=Chamada de Prova\n23= Trancamento\n24=Transferência\n25=Outros \n26=Matrícula Vínculo Institucional')).strip()

print()

# Verificando tipo de requerimento



if usuario == '1':
    request=req1
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '2':
    request=req2
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '3':
    request=req3
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '4':
    request=req4
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '5':
    request=req5
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '6':
    request=req6
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '7':
    request=req7
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '8':
    request=req8
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '9':
    request=req9
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '10':
    request=req10
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '11':
    request=req11
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '12':
    request=req12
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '13':
    request=req13
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '14':
    request=req14
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '15':
    request=req15
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '16':
    request=req16
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '17':
    request=req17
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '18':
    request=req18
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '19':
    request=req19
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '20':
    request=req20
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')
    
elif usuario == '21':
    request=req21
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '22':
    request=req22
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '23':
    request=req23
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '24':
    request=req24
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')
    
elif usuario == '25':
    request=req25
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

elif usuario == '26':
    request=req26
    aluno_requerente = Requisição()
    aluno_requerente.dados_do_requerente()
    aluno_requerente.verify_requests()
    print()
    print('='*60)
    print()
    print(f'Aluno: {aluno_requerente.nome}')
    print()
    print(f'Matrícula nº: {aluno_requerente.matricula}\n')
    print('Solicitação de requerimento Finalizada')

else:
    print('desculpe tente novamente')