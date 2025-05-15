# import flet as ft
# from flet import AppBar, Text, View
# from flet.core.colors import Colors
# from objeto import Pessoa
#
#
# def main(page: ft.Page):
#     # Configurações
#     page.title = "Exemplo de listas"
#     page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
#     page.window.width = 375
#     page.window.height = 667
#
#
#     # Funções
#
#     lista_pessoas = []
#
#     def salvar_nome(e):
#         print("passou")
#         if input_nome.value == '' or input_profissao.value == '' or input_salario.value == '':
#
#             page.overlay.append(msg_error)
#             msg_error.open = True
#             print("vazio")
#             page.update()
#         else:
#             print('else')
#             pessoa = Pessoa(input_nome.value, input_profissao.value, input_salario.value)
#             lista_pessoas.append(pessoa)
#             input_nome.value = ""
#             input_profissao.value = ""
#             input_salario.value = ""
#             page.overlay.append(msg_sucesso)
#             msg_sucesso.open = True
#             page.update()
#
#         print("Atualizou")
#
#     def exibir_lista():
#         lv_nome.controls.clear()
#         page.overlay.clear()
#         txt.value = ''
#         if lista_pessoas:
#             print('if exibir')
#             for pessoa in lista_pessoas:
#                 # print(nome)
#                 print(pessoa.nome)
#                 lv_nome.controls.append(
#                     ft.ListTile(
#                         leading=ft.Icon(ft.Icons.PERSON),
#                         title=ft.Text(value=pessoa.nome),
#                         subtitle=ft.Text(value=pessoa.profissao),
#                         trailing=ft.Button(
#                             ft.Icons.INFO,
#                             on_click=lambda _, n=pessoa.nome, p=pessoa.profissao, s=pessoa.salario: exibir_detalhes(n,
#                                                                                                                     p,
#                                                                                                                     s)
#                         ),
#                     ),
#                 )
#             page.update()
#         else:
#             txt.value = 'Não existem dados adicionados ainda'
#             page.overlay.append(txt)
#
#         print('update')
#         page.update()
#
#
#     def exibir_detalhes(nome, profissao, salario):
#         txt_nome.value = nome
#         txt_profissao.value = profissao
#         txt_salario.value = salario
#         page.go('/detalhes')
#
#     def ir_para_exibir():
#         page.views.clear()
#         exibir_lista()
#         page.go('/')
#
#
#     #  **********************************************
#     # *************************************************
#
#     def gerencia_rotas(e):
#         page.views.clear()
#         exibir_lista()
#         page.views.append(
#             View(
#                 "/",
#                 [
#                     AppBar(title=Text("Lista"), bgcolor=Colors.SECONDARY_CONTAINER),
#                     lv_nome,
#                     fab_adicionar
#                 ],
#             )
#         )
#         if page.route == "/adicionar" or page.route == "/detalhes":
#             txt.value = ''
#             page.views.append(
#                 View(
#                     "/adicionar",
#                     [
#                         AppBar(title=Text("Cadastro"), bgcolor=Colors.PRIMARY_CONTAINER),
#                         input_nome,
#                         input_profissao,
#                         input_salario,
#                         ft.Button(text='Salvar', on_click=lambda _: salvar_nome(e)),
#                         ft.Button(text='Exibir', on_click=lambda _: exibir_lista(e))
#
#                     ],
#                 )
#             )
#         elif page.route == "/detalhes":
#             page.views.append(
#                 View(
#                     '/detalhes',
#                     [
#                         AppBar(title=Text("Detalhes"), bgcolor=Colors.PRIMARY_CONTAINER),
#                         ft.Container(
#                             content=ft.Column(
#                                 [
#                                     txt_nome,
#                                     txt_profissao,
#                                     txt_salario,
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         page.update()
#
#     def voltar(e):
#         page.views.pop()
#         top_view = page.views[-1]
#         page.go(top_view.route)
#
#
#
#     # Componentes
#     lv_nome = ft.ListView(
#         height=500,
#         spacing=1,
#         divider_thickness=1
#     )
#     input_nome = ft.TextField(label="Nome:")
#     input_profissao = ft.TextField(label="Profissão:")
#     input_salario = ft.TextField(label="Salario:")
#
#     txt_nome = ft.Text()
#     txt_profissao = ft.Text()
#     txt_salario = ft.Text()
#
#     msg_sucesso = ft.SnackBar(
#         content=ft.Text('Salvo com sucesso!'),
#         bgcolor="green",
#     )
#     msg_error = ft.SnackBar(
#         content=ft.Text('Ocorreu um erro!'),
#         bgcolor=Colors.RED,
#     )
#     fab_adicionar = ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda _: page.go('/adicionar'))
#     txt = ft.Text()
#     # Eventos
#     page.on_route_change = gerencia_rotas
#     page.on_view_pop = voltar
#
#     page.go(page.route)
#
#
# # Comando que executa o aplicativo
# # Deve estar sempre colado na linha
# ft.app(main)
