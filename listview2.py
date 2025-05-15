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
            select_pessoa = select(Pessoa)
            pessoa = db_session.execute(select_pessoa).scalars()
            resultado = []
            for p in pessoa:
                resultado.append(p.serialize_pessoa())
            print(resultado)
            if not resultado:
                txt.value = 'Sem dados'
                page.overlay.clear()
                page.overlay.append(txt)
            else:
                txt.value = ''
                page.overlay.clear()
                print('select')
                for p in pessoa:
                    lv_pessoa.controls.append(
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.PERSON),
                            title=ft.Text(value=p.nome),
                            subtitle=ft.Text(value=p.profissao),
                        )
                    )
            page.update()
            page.views.clear()
        except Exception as e:
            print(e)
        finally:
            page.update()
            db_session.close()
            page.go('/exibir')


    def salvar_nome():
        db_session = local_session()
        try:
            form_add = Pessoa(nome=input_nome.value,
                              profissao=input_profissao.value,
                              salario=float(input_salario.value))
            form_add.save(db_session)
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
        except Exception as e:
            print(e)
            page.overlay.append(msg_error)
            msg_error.open = True
        finally:
            page.update()
            db_session.close()

    #  **********************************************
    # *************************************************

    def gerencia_rotas(e):
        page.views.clear()

        if page.route == '/':
            pagina_inicial()

        if page.route == '/exibir' or page.route == '/adicionar':
            page.views.append(
                View(
                    '/exibir',
                    [
                        AppBar(title=Text("Exibir"), bgcolor=Colors.PRIMARY_CONTAINER),
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda _: page.go('/adicionar')),
                        lv_pessoa
                    ]
                )
            )

        elif page.route == "/adicionar" or page.route == "/detalhes":
            page.views.append(
                View(
                    "/adicionar",
                    [
                        AppBar(title=Text("Cadastro"), bgcolor=Colors.PRIMARY_CONTAINER),
                        input_nome,
                        input_profissao,
                        input_salario,
                        ft.Button(text='Salvar', on_click=lambda _: salvar_nome()),
                        ft.Button(text='Exibir', on_click=lambda _: pagina_inicial())

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
                                    txt_nome,
                                    txt_profissao,
                                    txt_salario,
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
    lv_pessoa = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1
    )
    input_nome = ft.TextField(label="Nome:")
    input_profissao = ft.TextField(label="Profissão:")
    input_salario = ft.TextField(label="Salario:")

    txt_nome = ft.Text()
    txt_profissao = ft.Text()
    txt_salario = ft.Text()

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
