import flet as ft
from flet.core.types import MainAxisAlignment


def main(page: ft.Page):

    # Configuração da página
    page.title = 'Atividade 3'
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    # Definição de funções
    def exibir(valor, status):
        if status:
            txt_resultado.value = 'RESULTADO: ' + str(valor)
        else:
            txt_resultado.value = 'ERRO DE VALOR'
        page.update()

    def soma(e):
        num1 = input_num1.value
        num2 = input_num2.value
        try:
            num1 = int(num1)
            num2 = int(num2)
            print('try')
            exibir(num2 + num1, True)

        except ValueError:
            print('except')
            exibir(0, False)

    def sub(e):
        num1 = input_num1.value
        num2 = input_num2.value
        try:
            num1 = int(num1)
            num2 = int(num2)
            exibir(num1 - num2, True)
        except ValueError:
            exibir(0, False)

    def mult(e):
        num1 = input_num1.value
        num2 = input_num2.value
        try:
            num1 = int(num1)
            num2 = int(num2)
            exibir(num1 * num2, True)
        except ValueError:
            exibir(0, False)

    def div(e):
        num1 = input_num1.value
        num2 = input_num2.value
        try:
            num1 = int(num1)
            num2 = int(num2)
            if num2 != 0:
                exibir(num1 / num2, True)
            else:
                raise ValueError
        except ValueError:
            exibir(0, False)

    # Criação de componentes
    input_num1 = ft.TextField(label='Insira um número: ', hint_text='Ex.: 1, 2...', col=6)
    input_num2 = ft.TextField(label='Insira um número: ', hint_text='Ex.: 1, 2...', col=6)
    btn_soma = ft.ElevatedButton(text='Soma',
                                   width=page.window.width,
                                   on_click=soma,
                                   col=5)
    btn_sub= ft.ElevatedButton(text='Subtração',
                                 width=page.window.width,
                                 on_click=sub,
                                 col=5)
    btn_mult = ft.ElevatedButton(text='Multiplicação',
                                width=page.window.width,
                                on_click=mult,
                                 col=5)
    btn_div = ft.ElevatedButton(text='Divisão',
                                 width=page.window.width,
                                 on_click=div,
                                 col=5)
    txt_resultado = ft.Text(value='', size=24)
    # Construir o layout
    page.add(
        ft.Column(
            [
            ft.ResponsiveRow(
                [input_num1, input_num2],

            ),
            ft.ResponsiveRow(
                [btn_soma, btn_sub],
                alignment=MainAxisAlignment.CENTER,

            ),
            ft.ResponsiveRow(
                [btn_mult, btn_div],
                alignment=MainAxisAlignment.CENTER,
            ),
            ft.ResponsiveRow(
                [txt_resultado],
                alignment=MainAxisAlignment.CENTER,
            )
            ]
        )
    )

ft.app(main)