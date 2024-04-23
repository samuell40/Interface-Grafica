from guizero import App, Window, Text, TextBox, PushButton, Box


def testar_senha(event_data):
    if event_data.key == '\r':
        autenticar()




def autenticar():
    if usuario.value == '' or senha.value == '':
        app.error('Erro!', 'Os campos não podem estar vazios.')
    else:
        if autenticacao(usuario.value, senha.value):
            app.hide()
            principal.show()
        else:
            app.info('Acesso negado', 'Usuário e/ou senha estão incorretos, ou o usuário não está cadastrado.')


def abrir_cad():
    cadastro.show(wait=True)




def cadastrar():
    if codigo_cad.value == '' or usuario_cad.value == '' or senha_cad.value == '':
        cadastro.error('Erro!', 'Os campos não podem estar vazios.')
    else:
        if verificar_codigo(codigo_cad.value):
            if verificar_usuario(usuario_cad.value):
                cadastrar_usuario(codigo_cad.value, usuario_cad.value, senha_cad.value)
                cadastro.info('Operação realizada', 'Usuário cadastrado com sucesso!')
            else:
                cadastro.error('Erro!', 'Usuário já existe.')
        else:
            cadastro.error('Erro!', 'Código já existe.')




def abrir_busca():
    busca.show(wait=True)




def buscar():
    if usuario_busc.value == '':
        busca.error('Erro!', 'Os campos não podem estar vazios.')
    else:
        if buscar_usuario(usuario_busc.value):
            resultado = buscar_usuario(usuario_busc.value)
            busca.info('Resultado da Busca', f'{resultado}')
        else:
            busca.error('Erro!', 'Usuário não encontrado.')




def abrir_exc():
    exclusao.show(wait=True)



def excluir():
    if codigo_exc.value == '':
        exclusao.error('Erro!', 'Os campos não podem estar vazios.')
    else:
        if verificar_codigo(codigo_exc.value):
            exclusao.error('Erro!', f'Usuário com código {codigo_exc.value} não existe.')
        else:
            excluir_usuario(codigo_exc.value)
            exclusao.info('Sucesso!', f'Usuário com código {codigo_exc.value} excluído.')



def fechar_app():
    app.destroy()
