import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors


class User:
    def __init__(self, nome, profissao, salario):
        self.nome = nome
        self.profissao = profissao
        self.salario = salario

def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    def gerencia_rotas(e):
        exibir_lista(e)
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Lista"), bgcolor=Colors.SECONDARY_CONTAINER),
                    lv_nome,
                    fab_adicionar
                ],
            )
        )
        if page.route == "/adicionar":
            txt.value = ''
            page.views.append(
                View(
                    "/adicionar",
                    [
                        AppBar(title=Text("Cadastro"), bgcolor=Colors.PRIMARY_CONTAINER),
                        input_nome,
                        input_profissao,
                        input_salario,
                        ft.Button(text='Adicionar', on_click=lambda _: salvar_nome()),
                        # ft.Button(text='Exibir', on_click=lambda _: page.go('/'))

                    ],
                )
            )
        elif page.route == "/detalhes":
            page.views.append(
                View(
                    "/detalhes",
                    [
                        AppBar(title=Text("Detalhes"), bgcolor=Colors.PRIMARY_CONTAINER),
                        nome_detalhes,
                        profissao_detalhes,
                        salario_detalhes,

                    ]
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # ************************************************************************
    # ************************************************************************
    lista_users = []

    def salvar_nome():
        print("passou")

        if input_nome.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            print("vazio")
        else:
            user = User(nome=input_nome.value, profissao=input_profissao.value, salario=input_salario.value)
            lista_users.append(user)
            input_nome.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
        page.go('/')
        print("Atualizou")
        page.update()

    def exibir_lista(e):
        page.overlay.clear()
        lv_nome.controls.clear()
        txt.value = ''
        if lista_users:
            for user in lista_users:
                lv_nome.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON),
                        title=ft.Text(value=user.nome),
                        subtitle=ft.Text(user.profissao),
                        trailing=ft.IconButton(icon=ft.Icons.INFO, on_click=converter_obj(user)),
                    ),
                )
        else:
            txt.value = 'Não existem dados adicionados ainda'
            page.overlay.append(txt)
        page.update()

    def converter_obj(obj):
        nome_detalhes.value = obj.nome
        salario_detalhes.value = obj.salario
        profissao_detalhes.value = obj.profissao
        # page.go('/detalhes')
        page.update()

    # Componentes
    lv_nome = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1
    )
    input_nome = ft.TextField(label="Nome:")
    msg_sucesso = ft.SnackBar(
        content=ft.Text('Salvo com sucesso!'),
        bgcolor="green",
    )
    msg_error = ft.SnackBar(
        content=ft.Text('Ocorreu um erro!'),
        bgcolor=Colors.RED,
    )
    fab_adicionar = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda _: page.go('/adicionar'))
    txt = ft.Text()
    input_profissao = ft.TextField(label="Profissao:")
    input_salario = ft.TextField(label="Salário:")

    nome_detalhes = ft.Text()
    salario_detalhes = ft.Text()
    profissao_detalhes = ft.Text()

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)


# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
