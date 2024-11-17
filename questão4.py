print('Bem-vindos a empresa da Eshiley Mara Rodrigues')

#CRIAÇÃO DA LISTA E VARIÁVEL
lista_funcionarios = []
id_global = 4931764

#FUNÇÃO
def cadastrar_funcionario(id):
        
        #ENTRADA
        print('\n\n------------- MENU DE CADASTRO -------------')
        nome = input('Digite o nome: ')
        setor = input('Digite o setor: ')
        salário = input('Digite o salário base: ')

        #DICIONÁRIO
        dict_funcionarios = {
            "id": id,
            "nome": nome,
            "setor": setor,
            "salário": salário,
        }

        #LIGAÇÃO
        lista_funcionarios.append(dict_funcionarios.copy())
        print('\nFuncionário cadastrado com sucesso!','\nRetornando ao menu...')
        return ''
#FUNÇÃO
def consultar_funcionarios():
        while True:
        
            #ENTRADA
            print('\n\n----------- MENU DE CONSULTA -----------','\n1. Consultar Todos','\n2. Consultar por Id','\n3. Consultar por Setor', '\n4. Retornar ao menu')
            res = input('>> ')
            
            #CONDIÇÃO
            if res == '1':

                #RETORNE TODOS OS FUNCIONÁRIOS
                for func in lista_funcionarios:
                    print(f'\nID: {func["id"]}', f'\nNome: {func["nome"]}', f'\nSetor: {func["setor"]}', f'\nSalário: {func["salário"]}\n')
            
            #CONDIÇÃO
            elif res == '2':
                busca_id = input('Escreva o ID: ')
                trueshy = False
                
                #PARA FUNCIONÁRIO EM LISTA(Pensei aqui que, é necessário chamar a lista para a máquina saber onde buscar), SE, A ENTRADA CONCIDIR COM ID DE UM FUNCIONÁRIO CADASTRADO, RETORNE-O
                for func in lista_funcionarios:
                    if str(func["id"]) == busca_id:
                            trueshy = True
                            print(f'\nNome: {func["nome"]}', f'\nSetor: {func["setor"]}', f'\nSalário: {func["salário"]}')
                    else:
                         if trueshy == False:
                            print('\nID não encontrado.')
            #CONDIÇÃO
            elif res == '3':
                busca_setor = input('Escreva o setor: ')
                trueshy = False
                
                #PARA FUNCIONÁRIO EM LISTA(Pensei aqui que, é necessário chamar a lista para a máquina saber onde buscar), SE, A ENTRADA CONCIDIR COM OS FUNCIONÁRIOS CADASTRADOS NO SETOR, RETORNE-OS
                for func in lista_funcionarios:
                        if func["setor"] == busca_setor:
                            trueshy = True
                            print(f'\nID: {func["id"]}', f'\nNome: {func["nome"]}', f'\nSalário: {func["salário"]}\n')
                        else:
                            if trueshy == False:
                                print('Setor não encontrado.')
            #CONDIÇÃO
            elif res == '4':
                return ''
            else:
                print('\nOpção inválida.')
                continue

#FUNÇÃO
def remover_funcionarios():
    while True:
        
        print('\n\n--------------- INATIVAR CADASTRO ---------------')
        # ENTRADA
        remove_id = str(input('Digite o ID do funcionário para removê-lo: '))
        achou = False
        
        # PARA FUNCIONÁRIO NA LISTA, SE COINCIDIR COM O ID, PEÇA CONFIRMAÇÃO ANTES DE EXCLUIR
        for func in lista_funcionarios:
            if str(func["id"]) == remove_id:
                print('\nGostaria de remover este funcionário(a)?', f'\nNome: {func["nome"]}', f'\nSetor: {func["setor"]}')
                confirmacao = input('\n(S/N): ').upper()
                achou = True
                
                #CONDIÇÃO
                if confirmacao == 'S':
                    lista_funcionarios.remove(func)
                    print('\nRemovido com sucesso.')
                    break
                elif confirmacao == 'N':
                    return ''
            
        #RETORNAR AO MENU    
        if not achou and remove_id == '1':
            print('\nRetornando ao menu...')
            return ''
                
        if not achou:
            print('\nFuncionário não encontrado. Tente novamente.', '\n(Para retornar ao menu digite 1.)\n')
                 
                    
                    

            
#MAIN
while True:
    print('\n--------- MENU -----------',
          '\n1. Cadastrar funcionário',
          '\n2. Consultar funcionário',
          '\n3. Remover funcionário',
          '\n4. Sair',)
    res = input('>> ')

    #CONDIÇÃO
    if res == '1':
        id_global += 1
        print(cadastrar_funcionario(id_global))
    elif res == '2':
        print(consultar_funcionarios())
    elif res == '3':
        print(remover_funcionarios())
    elif res == '4':
        exit()
    else:
        print('Escolha uma das opções (1, 2, 3 ou 4). Tente novamente.') 