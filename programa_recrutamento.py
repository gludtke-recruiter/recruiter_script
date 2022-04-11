#Este programa vai nos auxiliar no processo de recrutamento e Seleção
x=1

while x==1:

    print('Seja Bem-vindo(a)\n')
    print('Este programa vai ajudar a realizar o processo de R&S da Cielo')

    e_superior= int(input(('Pergunta 1) O candidato esta cursando ou Cursou o Ensino Superior ? (1-SIM| 2- NAO) \n')))
    c_comercial= int(input(('Pergunta 2) O candidato Tem experiencia na Area Comercial ? (1-SIM| 2- NAO) \n')))
    c_carteira= int(input(('Pergunta 3) O candidato Tem experiencia com gerenciamento de carteira de clientes? (1-SIM| 2- NAO) \n')))
    e_externa=  int(input(('Pergunta 4) O candidato Tem experiencia com Vendas Externas ? (1-SIM| 2- NAO) \n')))
    h_carro= int(input(('Pergunta 5) O candidato Tem Habilitacao B e Carro proprio ? (1-SIM| 2- NAO) \n')))

    if (e_superior == 1 and c_comercial == 1 and c_carteira == 1 and e_externa == 1 and h_carro == 1):
        print('CANDIDATO APROVADO ------ O candidato possui todos os pre=requisitos tecnicos - avaliar fit cultural agora')
    if (e_superior == 2):
        print('CANDIDATO REPROVADO -- Sem curso Superior')
    if (c_comercial == 2):
        print('CANDIDATO REPROVADO -- Sem experiencia comercial')
    if (c_carteira == 2):
        print('CANDIDATO REPROVADO -- Sem experiencia com carteira de clientes')
    if (e_externa == 2):
        print('CANDIDATO REPROVADO -- Sem Experiencia externa')
    if (h_carro == 2):
        print('CANDIDATO REPROVADO -- Sem veiculo ou habilitacao')

            
