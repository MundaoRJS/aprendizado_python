def ler_arquivos():
    arquivos = 'C:\Users\raimu\Documents\projeto -final\aprendizado_python'
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