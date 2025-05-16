import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
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
            select_livro = select(Livro)
            livros = db_session.execute(select_livro).scalars().all()
            # resultado = []
            # for p in pessoa:
            #     resultado.append(p.serialize_pessoa())
            # print(resultado)
            if not livros:
                txt.value = 'Sem dados'
                page.overlay.clear()
                page.overlay.append(txt)
            else:
                txt.value = ''
                page.overlay.clear()
                print('select')
                lv_livros.controls.clear()
                for livro in livros:

                    lv_livros.controls.append(
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.BOOK),
                            title=ft.Text(value=livro.titulo),
                            # trailing=ft.Button(text='Detalhes', on_click=lambda _, l=livro: detalhes(l))
                            trailing=ft.PopupMenuButton(
                                icon=ft.Icons.MORE_VERT, icon_color=Colors.BLACK,
                                items=[
                                    ft.PopupMenuItem(text=f'Detalhes',
                                                     on_click=lambda _, l=livro: detalhes(l)),

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

    def salvar_livro():
        db_session = local_session()

        try:
            form_add = Livro(
                titulo=input_titulo.value,
                descricao=input_descricao.value
            )
            form_add.save(db_session)
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            input_titulo.value = ''
            input_descricao.value = ''
        except Exception as e:
            print(e)
            page.overlay.append(msg_error)
            msg_error.open = True
        finally:
            db_session.close()
            pagina_inicial()

    def navegar_salvar(e):
        page.go('/salvar')


    def detalhes(livro):
        db_session = local_session()
        try:
            sql = select(Livro).where(Livro.id_livro == livro.id_livro)
            livro = db_session.execute(sql).scalar()
            txt_titulo.value = livro.titulo
            txt_descricao.value = livro.descricao
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
                        AppBar(title=Text("Exibir"), bgcolor=Colors.PRIMARY_CONTAINER),
                        lv_livros,
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda _: navegar_salvar(e))
                    ]
                )
            )

        elif page.route == "/salvar":
            txt.value = ''
            page.views.append(
                View(
                    "/salvar",
                    [
                        AppBar(title=Text("Cadastro"), bgcolor=Colors.PRIMARY_CONTAINER),
                        input_titulo,
                        input_descricao,
                        ft.Button(text='Salvar', on_click=lambda _: salvar_livro()),
                        ft.Button(text='Voltar', on_click=lambda _: pagina_inicial())

                    ],
                )
            )
        elif page.route == "/detalhes":
            page.views.append(
                View(
                    '/detalhes',
                    [
                        AppBar(title=Text("Detalhes"), bgcolor=Colors.PRIMARY_CONTAINER),
                        ft.Container(
                            content=ft.Column(
                                [
                                    txt_titulo,
                                    txt_descricao,
                                    ft.Button(text='Voltar', on_click=lambda _: pagina_inicial())

                                ]
                            )
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
    lv_livros = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1
    )
    input_titulo = ft.TextField(label="Título:")
    input_descricao = ft.TextField(label="Decrição:")

    txt_titulo = ft.Text()
    txt_descricao = ft.Text()

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
