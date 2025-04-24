import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors


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
                        ft.Button(text='Salvar', on_click=lambda _: salvar_nome(e)),
                        ft.Button(text='Exibir', on_click=lambda _: page.go('/'))

                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # ************************************************************************
    # ************************************************************************
    lista_nomes = []

    def salvar_nome(e):
        print("passou")
        if input_nome.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            print("vazio")
        else:
            lista_nomes.append(input_nome.value)
            input_nome.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True

        print("Atualizou")
        input_nome.value = 'TESTEEEEE'
        page.update()

    def exibir_lista(e):
        lv_nome.controls.clear()
        txt.value = ''
        if lista_nomes:
            for nome in lista_nomes:
                lv_nome.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON),
                        title=ft.Text(value=nome),
                        subtitle=ft.Text('User'),

                    ),
                )
        else:
            txt.value = 'Não existem dados adicionados ainda'
            page.overlay.append(txt)
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
    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)


# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
