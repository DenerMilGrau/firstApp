import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from flet.core.types import FontWeight

from models import Pessoa, Livro, local_session
from sqlalchemy import select


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de listas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    def pagina_inicial():
        db_session = local_session()
        try:
            select_pessoa = select(Pessoa)
            pessoas = db_session.execute(select_pessoa).scalars().all()
            # resultado = []
            # for p in pessoa:
            #     resultado.append(p.serialize_pessoa())
            # print(resultado)
            if not pessoas:
                txt.value = 'Sem dados'
                page.overlay.clear()
                page.overlay.append(txt)
            else:
                txt.value = ''
                page.overlay.clear()
                print('select')
                lv_pessoa.controls.clear()
                for p in pessoas:
                    print(p.nome)
                    print(p.id)
                    lv_pessoa.controls.append(
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.PERSON),
                            title=ft.Text(value=p.nome),
                            subtitle=ft.Text(value=p.profissao),
                            trailing=ft.PopupMenuButton(
                                icon=ft.Icons.MORE_VERT, icon_color="white",
                                items=[
                                    ft.PopupMenuItem(text=f'Detalhes',
                                                     on_click=lambda _, u=p: detalhes(u)),

                                ],
                        )   )
                    )
            page.update()
            page.views.clear()
        except Exception as e:
            print(e)
        finally:
            db_session.close()
            page.go('/exibir')

    def salvar_nome():
        db_session = local_session()

        try:
            page.overlay.clear()
            form_add = Pessoa(
                nome=input_nome.value,
                profissao=input_profissao.value,
                salario=float(input_salario.value)
            )
            form_add.save(db_session)
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            pagina_inicial()
        except Exception as e:
            print(e)
            page.overlay.append(msg_error)
            msg_error.open = True
        finally:
            db_session.close()

    def navegar_adicionar(e):
        page.go('/adicionar')


    def detalhes(pessoa):
        db_session = local_session()
        try:
            print(pessoa)
            # print(id_user)
            sql = select(Pessoa).where(Pessoa.id == pessoa.id)
            usuario = db_session.execute(sql).scalar()
            print(usuario)
            txt_profissao.value = usuario.profissao
            txt_nome.value = usuario.nome
            txt_salario.value = 'R$' + '' + str(usuario.salario).replace('.', ',')
            page.go('/detalhes')
        except Exception as e:
            print(e)



    #  **********************************************
    # *************************************************
    def gerencia_rotas(e):
        page.views.clear()

        if page.route == '/':
            pagina_inicial()

        elif page.route == '/exibir':
            page.views.append(
                View(
                    '/exibir',
                    [
                        AppBar(title=Text("Exibir"), bgcolor="#6959CD"),
                        lv_pessoa,
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda _: navegar_adicionar(e),bgcolor="#6959CD"),
                    ]
                )
            )

        elif page.route == "/adicionar":
            print('\nVIEW ADICIONAR\n')
            txt.value = ''
            page.views.append(
                View(
                    "/adicionar",
                    [
                        AppBar(title=Text("Cadastro"), bgcolor="#6959CD"),
                        input_nome,
                        input_profissao,
                        input_salario,
                        ft.Button(text='Salvar', on_click=lambda _: salvar_nome()),
                        ft.Button(text='Voltar', on_click=lambda _: pagina_inicial())

                    ],
                )
            )
        elif page.route == "/detalhes":
            page.views.append(
                View(
                    '/detalhes',
                    [
                        AppBar(title=Text("Detalhes"), bgcolor="#6959CD"),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text('Nome:', size=24, weight=FontWeight.BOLD),
                                    txt_nome,
                                    ft.Text('Profissão:', size=24, weight=FontWeight.BOLD),
                                    txt_profissao,
                                    ft.Text('Salário', size=24, weight=FontWeight.BOLD),
                                    txt_salario,
                                    ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Button(text='Voltar', on_click=lambda _: pagina_inicial())
                                            ]
                                        ),
                                        padding=ft.padding.only(top=120)  # Ajuste para mover um pouco para baixo
                                    )


                                ],
                                alignment=ft.MainAxisAlignment.CENTER,  # Alinha no centro verticalmente
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alinha no centro horizontalmente
                            ),
                            alignment=ft.alignment.center,  # Centraliza o Container
                            padding=ft.padding.only(top=80)  # Ajuste para mover um pouco para baixo
                        )
                    ]
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # Componentes
    lv_pessoa = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1
    )
    input_nome = ft.TextField(label="Nome:")
    input_profissao = ft.TextField(label="Profissão:")
    input_salario = ft.TextField(label="Salario:")

    txt_nome = ft.Text('', size=22)
    txt_profissao = ft.Text('', size=22)
    txt_salario = ft.Text('', size=22)

    msg_sucesso = ft.SnackBar(
        content=ft.Text('Salvo com sucesso!'),
        bgcolor="green",
    )
    msg_error = ft.SnackBar(
        content=ft.Text('Ocorreu um erro!'),
        bgcolor=Colors.RED,
    )
    # fab_adicionar = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda _: page.go('/adicionar'))
    txt = ft.Text('Sem dados')
    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)


# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
