import flet as ft


def main(page: ft.Page):

    # Configuração da página
    page.title = 'Atividade 2'
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    # Definição de funções
    def verificar_num(e):
        num = input_num.value
        try:
            num = int(num)
            if num % 2 == 0:
                txt_resultado.value = 'É par !'
            else:
                txt_resultado.value = 'É ímpar !'
        except ValueError:
            txt_resultado.value = 'insira um número válido'
        page.update()
    # Criação de componentes
    input_num = ft.TextField(label='Insira um número: ', hint_text='Ex.: 1, 2...')
    btn_enviar = ft.ElevatedButton(text='Enviar',
                                   width=page.window.width,
                                   on_click=verificar_num)
    txt_resultado = ft.Text(value='', size=24)
    # Construir o layout
    page.add(
        ft.Column(
            [input_num, btn_enviar, txt_resultado]
        )
    )

ft.app(main)