def autenticacao(usuario, senha):
    try:
        with open('lista_usuarios.txt', 'r') as lista:
            for i in lista:
                linha = i.split()
                if usuario == linha[1] and senha == linha[2]:
                    return True
    except FileNotFoundError:
        with open('lista_usuarios.txt', 'a') as lista:
            lista.write('0 admin 123\n')
        return False


def cadastrar_usuario(codigo, usuario, senha):
    try:
        with open('lista_usuarios.txt', 'a') as usuarios:
            usuarios.write(f'{codigo} {usuario} {senha}\n')
    except Exception as e:
        print(f'Erro: {e}.')


def buscar_usuario(usuario):
    try:
        with open('lista_usuarios.txt', 'r') as lista:
            for i in lista:
                linha = i.split()
                if usuario == linha[1]:
                    return f'Código: {linha[0]}\nUsuário: {linha[1]}'
            else:
                print('Usuário não encontrado.')
                return False
    except Exception as e:
        print(f'Erro: {e}')
        return False


def excluir_usuario(codigo):
    repetido = False
    codigo_ex = ''
    nome_ex = ''
    senha_ex = ''

    with open('lista_usuarios.txt', 'r+') as usuarios:
        users = usuarios.readlines()


    with open('lista_usuarios.txt', 'w') as usuarios:
        for i in users:
            codigo_user, usuario, senha = i.strip('\n').split(' ')
            if codigo == codigo_user:
                print(codigo_user)
                codigo_user = codigo_ex
                usuario = nome_ex
                senha = senha_ex
                repetido = True

            else:
                usuarios.write(i)

        if repetido == True:
            return repetido
        else:
            return repetido


def listar():
    with open('lista_usuarios.txt', 'r') as lista:
        usuarios = lista.readlines()
        return usuarios
