

# escola

# cadastro

acesso = input('Deseja acessar o sistema? s/n >>')

while acesso == 's':
    print('SISTEMA ESCOLA xyz')

    nome = input('Nome Aluno 👤 >>') # variável
    # snake_case
    nota_1 = float(input('Nota 1>>'))
    nota_2 = float(input('Nota 2>>'))
    nota_3 = float(input('Nota 3>>'))

    #media
    lista = []
    lista.append(nota_1)
    lista.append(nota_2)
    lista.append(nota_3)

    media = sum(lista)/len(lista)

    print('O aluno(a)', nome, 'possui a media', media)

    if media >= 7:
        print(f"O {nome} Passou de ano 🥇 ")
    elif media >= 5 and media <7:
        print(f"O {nome} Está de recuperação 🚨 ")
    else:
        print(f"O {nome} não passou de ano... 😞 ")
    acesso = input('Deseja continuar? s/n >>')

print('Até logo...')
input('Clique enter para sair...')