from guizero import App, Window, Text, TextBox, PushButton, Box
from classe import verificar_codigo, verificar_usuario
from persistencia import autenticacao, cadastrar_usuario, buscar_usuario, excluir_usuario


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



# login
app = App(title='Login', height=130, width=300, bg='#dcdcdc')


bottom_box = Box(app, align='bottom', layout='grid')
top_box = Box(app, align='bottom', layout='grid')


Text(app, text='LOGIN', font='Georgia', grid=[1, 0], size=18, color='#606060')


Text(top_box, font='Georgia', text='Usuário: ', grid=[0, 1])
usuario = TextBox(top_box, width=30, grid=[1, 1])
Text(top_box, font='Georgia', text='Senha:', grid=[0, 2])
senha = TextBox(top_box, width=30, hide_text=True, grid=[1, 2])
senha.when_key_pressed = testar_senha


usuario.tk.config(bg='white')
senha.tk.config(bg='white')


enviar = PushButton(bottom_box, text='Enviar', command=autenticar, width=16, grid=[0, 0])
cadastro_btn = PushButton(bottom_box, text='Novo Usuário', command=abrir_cad, width=16, grid=[1, 0])


enviar.tk.config(bg='#b0b0b0')
cadastro_btn.tk.config(bg='#b0b0b0')


# principal
principal = Window(app, title='Janela Principal', width=350, height=210, bg='#dcdcdc')
box = Box(principal, align='bottom', layout='grid')
Text(principal, font='Georgia', text='JANELA PRINCIPAL', size='18', color='#606060', grid=[0, 0])


cadastro_btn2 = PushButton(box, image="./Imagens/adc_usuario.png", command=abrir_cad, width=100, height=55, grid=[0, 0])
Text(box, font='Georgia', text='Cadastrar Usuário', grid=[0, 1])


busca_btn = PushButton(box, image="./Imagens/lupa.png", command=abrir_busca, width=100, height=55, grid=[1, 0])
Text(box, font='Georgia', text='Buscar Usuário', grid=[1, 1])


excluir_btn = PushButton(box, image="./Imagens/lixeira.png", command=abrir_exc, width=100, height=55, grid=[0, 2])
Text(box, font='Georgia', text='Excluir Usuário', grid=[0, 3])


cancelar = PushButton(box, image="./Imagens/x.png", command=fechar_app, width=100, height=55, grid=[1, 2])
Text(box, font='Georgia', text='Encerrar Aplicação', grid=[1, 3])


cadastro_btn2.tk.config(bg='#b0b0b0')
busca_btn.tk.config(bg='#b0b0b0')
excluir_btn.tk.config(bg='#b0b0b0')
cancelar.tk.config(bg='#e74c3c')


principal.hide()
principal.when_closed = fechar_app


# cadastro
cadastro = Window(app, title='Cadastrar', bg='#dcdcdc', height=125, width=240)
cad_box = Box(cadastro, align='top', layout='grid')


Text(cad_box, font='Georgia', text='Código: ', grid=[0, 0])
codigo_cad = TextBox(cad_box, width=20, grid=[1, 0])
Text(cad_box, font='Georgia', text='Usuário: ', grid=[0, 1])
usuario_cad = TextBox(cad_box, width=20, grid=[1, 1])
Text(cad_box, font='Georgia', text='Senha: ', grid=[0, 2])
senha_cad = TextBox(cad_box, width=20, hide_text=True, grid=[1, 2])
cadastrar = PushButton(cadastro, text='Cadastrar', command=cadastrar, width=15)


cadastrar.tk.config(bg='#b0b0b0')
codigo_cad.tk.config(bg='white')
usuario_cad.tk.config(bg='white')
senha_cad.tk.config(bg='white')
cadastro.hide()


# buscar
busca = Window(app, title='Buscar', height=75, width=240, bg='#dcdcdc')
busca_box = Box(busca, align='top', layout='grid')


Text(busca_box, font='Georgia', text='Usuário: ', grid=[0, 0])
usuario_busc = TextBox(busca_box, width=20, grid=[1, 0])
buscar = PushButton(busca, text='Buscar', command=buscar, width=15)


buscar.tk.config(bg='#b0b0b0')
usuario_busc.tk.config(bg='white')
busca.hide()


# excluir
exclusao = Window(app, title='Excluir', height=75, width=240, bg='#dcdcdc')
exc_box = Box(exclusao, align='top', layout='grid')


Text(exc_box, font='Georgia', text='Código: ', grid=[0, 0])
codigo_exc = TextBox(exc_box, width=20, grid=[1, 0])
excluir = PushButton(exclusao, text='Excluir', command=excluir, width=15)


excluir.tk.config(bg='#b0b0b0')
codigo_exc.tk.config(bg='white')
exclusao.hide()


# display do app e proibição de redimensionamento
app.tk.resizable(False, False)
principal.tk.resizable(False, False)
cadastro.tk.resizable(False, False)
busca.tk.resizable(False, False)
exclusao.tk.resizable(False, False)
app.display()



