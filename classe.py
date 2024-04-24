from persistencia import listar


class Usuario:
    def __init__(self, codigo, usuario, senha):
        self.codigo = codigo
        self.usuario = usuario
        self.senha = senha


def verificar_codigo(codigo):
    usuarios = listar()
    print(usuarios)
    cadastro = True

    for i in usuarios:
        linha = i.split()
        print(linha)
        if codigo == linha[0]:
            cadastro = False
            break
    return cadastro


def verificar_usuario(usuario):
    usuarios = listar()
    print(usuarios)
    cadastro = True

    for i in usuarios:
        linha = i.split()
        print(linha)
        if usuario == linha[1]:
            cadastro = False
            break
    return cadastro
