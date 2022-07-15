listaPecas = []


# ____________ Começo Cadastrar Peças ______________*
def cadastrarPeca(cod):
    print('Bem-vindo ao Cadastro de Peças')
    print('O cod a ser cadastrado é: {}'.format(cod))
    nome = input('Digite o nome da peça: ')
    fabricante = input('Digite o nome do fabricante: ')
    valor = float(input('Digite o valor da peça: '))
    dicionarioPeca = {'cod': cod,
                      'nome': nome,
                      'fabricante': fabricante,
                      'valor': valor}
    listaPecas.append(dicionarioPeca.copy())


# _______________Fim Cadastrar Peças _______________*

# _________________Consultar Peças _________________*
def consultarPeca():
    while True:
        try:
            print('Bem-vindo a Consulta de Peças')
            opConsultar = int(input('Entre com a opção desejada:\n'
                                    '1- Consultar todas as Peças:\n'
                                    '2- Consultar Peças por código:\n'
                                    '3- Consultar Peças por Fabricante:\n'
                                    '4- Retornar'))
            if opConsultar == 1:
                print('Bem-Vindo a Consultar Todas as Peças ')
                for peca in listaPecas:
                    for key, value in peca.items():
                        print('{} : {}'.format(key, value))
            elif opConsultar == 2:
                print('Bem-Vindo a Consultar Peças Por Codigo')
                entrada = int(input('Digite o Código desejado:'))
                for peca in listaPecas:
                    if (peca['cod'] == entrada):
                        for key, value in peca.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 3:
                print('Bem-Vindo a Consultar Peças Por Fabricante')
                entrada = input('Digite o Fabricante desejado:')
                for peca in listaPecas:
                    if (peca['fabricante'] == entrada):
                        for key, value in peca.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 4:
                print('Retornar')
                return
            else:
                print('Pare de digitar números que não existem no menu!')
                continue
        except ValueError:
            print('Pare de digitar valores não inteiros')


# _______________ Fim Consultar Peças_______________*

# ________________Começo Remover Peças______________*
def removerPeca():
    print('Bem-vindo Remoção de Peças')
    entrada = int(input('Digite o Código desejado:'))
    for peca in listaPecas:
        if (peca['cod'] == entrada):
            listaPecas.remove(peca)


# ________________ Fim Remover Peças________________*

# _________________Começo da Main___________________*
print('Bem Vindo ao Controle de Estoque da Bicicletaria do Bruno G Santos')
registroPeca = 0
while True:
    try:
        opcao = int(
            input('Digite a opção desejada:\n1-Cadastrar Peças:\n2-Consultar Peças:\n3-Remover Peças:\n4-Sair: '))
        if opcao == 1:
            registroPeca = registroPeca + 1
            cadastrarPeca(registroPeca)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Programa finalizado')
            break
        else:
            print('Pare de digitar números que não existem no menu!')
            continue

    except ValueError:
        print('Pare de digitar valores não inteiros')
