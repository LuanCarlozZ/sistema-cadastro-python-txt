
def cadastrar():
    usuarios = {}
    usuarios['nome'] = input('Digite seu nome: ')

    while True:
        try:
                usuarios['idade'] = int(input('Digite sua idade: '))
                break
        except Exception as error:
                print('Digite um numero!')

    usuarios['curso'] = input('Digite seu curso: ')
    print('Usuário cadastrado!')


    with open('arquivo.txt', 'a') as arquivo:
                arquivo.write(f'Nome: {usuarios["nome"]}\n')
                arquivo.write(f'Idade: {usuarios["idade"]}\n')
                arquivo.write(f"Curso: {usuarios['curso']}\n")
                arquivo.write('\n')


while True:
    print('\n ==== MENU  ======')
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Remover usuário")
    print("5 - Sair")

    opcao = input('Escolha uma Opção: ').strip()

    if opcao == '1':
        cadastrar()
            


    elif opcao == '2':
        with open('arquivo.txt', 'r') as arquivo:
              conteudo = arquivo.read()
              print(conteudo)
    

    elif opcao == '3':
        nome_procurado= input('Digite o nome que procura: ').strip().lower()
        with open('arquivo.txt', 'r') as arquivo:
             conteudo = arquivo.read()
             usuarios = conteudo.split('\n\n') 
             encontrado = False
             for usuario in usuarios:
                if nome_procurado in usuario.lower():
                  print("\n--- Usuário encontrado ---")
                  print(usuario)
                  encontrado = True
                if not encontrado:
                      print('Usuário não econtrado.')
               




    elif opcao == '4':
        nome_remover = input('Digite o nome que você quer remover. ').strip().lower()
        with open('arquivo.txt', 'r') as arquivo:
                    conteudo = arquivo.read()
                    usuarios = conteudo.split('\n\n')
                    usuarios_restantes = []

                    for usuario in usuarios:
                        if usuario.strip() != '':
                          if nome_remover not in usuario.lower():
                                usuarios_restantes.append(usuario)
                    conteudo_novo = '\n\n'.join(usuarios_restantes)
                                

        with open('arquivo.txt', 'w') as arquivo:
                    arquivo.write(conteudo_novo)
                    print('Usuário removido!')

    elif opcao == '5':
           break