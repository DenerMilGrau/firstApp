import flet as ft
from datetime import date

def main(page: ft.Page):

    # Configuração da página
    page.title = 'Atividade 4'
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    # Definição de funções
    def calcular_idade(e):
        data_nasc = input_data.value
        try:
            if len(data_nasc) == 10:
                print('if 1')
                barra_verif = '{}{}'.format(data_nasc[2:3], data_nasc[5:6])
                if barra_verif == '//':
                    print('if 2')
                    dia = '{}'.format(data_nasc[:2])
                    mes = '{}'.format(data_nasc[3:5])
                    ano = '{}'.format(data_nasc[6:])

                    data_atual = date.today()

                    if int(mes) < 0 or int(ano) < 0 or int(dia) < 0 or int(mes) > 12 or int(dia) > 31 or int(ano) > data_atual.year:
                        raise ValueError
                    else:
                        if int(ano) == data_atual.year and int(mes) > data_atual.month:
                            raise ValueError
                        elif int(ano) == data_atual.year and int(mes) == data_atual.month and int(dia) > data_atual.day:
                            raise ValueError
                        else:
                            idade = data_atual.year - int(ano)
                            print('idade: {}'.format(idade))
                            if idade > 120:
                                raise ValueError
                            else:
                                if data_atual.month < int(mes):
                                    print('if idade')
                                    idade -= 1
                                else:
                                    print('else')
                                    if data_atual.day < int(dia):
                                        print('if idade 2')
                                        idade -= 1
                                        print('idade segunda vez: {}'.format(idade))
                                txt_resultado.value = (f'IDADE: {str(idade)}\n'
                                                       f'{'Menor' if idade < 18 else 'Maior'} de idade')
            else:
                print('else')
                txt_resultado.value = 'data invalida'
        except ValueError:
            print('except value')
            txt_resultado.value = 'data invalida'
        page.update()

    # Criação de componentes
    input_data = ft.TextField(label='Insira sua data de nascimento: ', hint_text='Ex.: 20/01/1998')
    btn_calcular = ft.ElevatedButton(text='Calcular',
                                     width=page.window.width,
                                     on_click=calcular_idade,
                                     )
    txt_resultado = ft.Text(value='', size=24)

    # Construir layout
    page.add(
        ft.Column(
            [input_data, btn_calcular, txt_resultado]
        )
    )

ft.app(main)