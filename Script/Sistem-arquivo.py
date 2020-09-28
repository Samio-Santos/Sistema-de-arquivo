# Cria um arquivo txt.
def criar_arquivo(nome_arq):
    from termcolor import colored
    try:
        arq = open(f'{nome_arq}.txt', 'xt')
        arq.close()

    except FileExistsError:
        print(colored('ARQUIVO JÁ EXISTI ou OCORREU UM ERRO NA CRIAÇÃO DO ARQUIVO!', 'red'))


    else:
        print(colored(f'Arquivo {nome_arq}.xls criado com sucesso!', 'green'))


# Escreve em um arquivo txt
def escrever_arquivo(nome_arq):
    from termcolor import colored
    while True:
        arq = open(f'{nome_arq}.txt', 'at')
        nome = str(input('Nome: ')).capitalize().strip()
        idade = str(input('Idade: '))
        arq.write(f'{nome};{idade}\n')
        arq.close()
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        print('-=' * 30)
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

        if resp == 'N':
            break

    print(colored('CADASTRO FEITO COM SUCESSO!', 'green', attrs=['bold']))


# Ler dados inseridos no arquivo
def ler_arquvio(nome_arq):
    from termcolor import colored
    try:
        arq = open(f'{nome_arq}.txt', 'rt')

    except FileNotFoundError:
        print(colored('ERRO AO LER O ARQUIVO ou ARQUIVO NÃO ENCONTRADO!', 'red'))

    else:
        print(colored('PESSOAS CADASTRADAS'.center(50), 'green'))
        for p, i in enumerate(arq):
            dado = i.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{p + 1:<2}- {dado[0]:<40}{dado[1]:>3} anos')

        arq.close()


# Função para remover arquivos
def remover_arquivo(nome_ar):
    from termcolor import colored
    import os
    os.remove(f'{nome_ar}.txt')
    print(colored('ARQUIVO REMOVIDO COM SUCESSO!', 'red'))


# Cria uma linha
def linha():
    from termcolor import colored
    print(colored('-=' * 30, 'white', attrs=['bold']))


if __name__ == "__main__":
    # Modulo de cor
    from termcolor import colored

    while True:
        linha()
        print(colored('MENU PRINCIPAL'.center(55), 'white', attrs=['bold']))
        linha()
        print(colored('''
    1- Criar um arquivo
    2- Ver pessoas cadastras 
    3- Remover arquivo
    4- Cadastrar uma nova pessoa em um arquivo
    5- Sair do sistema''', 'blue'))
        linha()

        opcao = int(input('Digite a sua opção: '))

        while opcao > 5:
            print(colored('Erro! Digite uma opção válida.', 'red'))
            linha()
            opcao = int(input('Digite a sua opção: '))
        linha()

        if opcao == 1:
            criar_arquivo(str(input('Digite o nome do arquivo: ')))

        elif opcao == 2:
            while True:
                nome_arq = str(input('Digite o nome do arquivo que deseja ler os dados: '))
                linha()
                ler_arquvio(nome_arq)
                linha()
                print(colored('''Opção: 
                
    1- Consultar outro arquivo
    2- Voltar ao menu principal''', 'blue'))
                print('')
                resp = int(input('Digite a sua opção: '))
                if resp == 2:
                    break
        elif opcao == 3:
            remover_arquivo(str(input('Digite o nome do arquivo para ser removido: ')))

        elif opcao == 4:
            nome_arq = str(input('Digite o nome do arquivo para cadastrar uma nova pessoa: '))
            print('')
            try:
                arquivo = open(f'{nome_arq}.txt', 'rt')
                arquivo.close()
            except FileNotFoundError:
                linha()
                print(colored('ARQUIVO NÃO ENCONTRADO ou NÃO EXISTI!', 'red'))
            else:
                escrever_arquivo(nome_arq)

        elif opcao == 5:
            break

print(colored('>>> SISTEMA FINALIZADO COM SUCESSO <<<', 'green', attrs=['bold']))
