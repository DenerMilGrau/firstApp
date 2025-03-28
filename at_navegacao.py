import flet as ft

from flet.core.app_bar import AppBar
from flet import AppBar, ElevatedButton, Text, Colors, View


def main(page: ft.Page):

    # Configuração da página
    page.title = 'Atividade 4'
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    # Definição de funções
    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Home'), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text='navegar', on_click=lambda _: page.go('/segunda'))
                ]
            )
        )
        if page.route == '/segunda':
            page.views.append(
                View(
                    '/segunda',
                    [AppBar(title=Text('Segunda'), bgcolor=Colors.PRIMARY_CONTAINER)]
                )
            )
        page.update()
    def volta(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.go(page.route)
    page.on_view_pop = volta


    # Criação de componentes
#     input_data = ft.TextField(label='Insira sua data de nascimento: ', hint_text='Ex.: 20/01/1998')
#     btn_calcular = ft.ElevatedButton(text='Calcular',
#                                      width=page.window.width,
#                                      on_click=calcular_idade,
#                                      )
#     txt_resultado = ft.Text(value='', size=24)

    # Construir layout


ft.app(main)