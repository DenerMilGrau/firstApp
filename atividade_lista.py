# Etapa 1
# Criar lista com 3 itens
lista_objetos = ['mesa', 'garfo', 'varal', 'caixa', 'sofa'] # Ele reclama q eu n preciso de um append
                                          # Se posso adicionar direto na criação
print('Lista de objetos criada')
print(lista_objetos)

# Etapa 2
# Adicionar mais um item
lista_objetos.append('bacia')

# Etapa 3
# Acessar objeto da 2ª posição
print('\n2ª posição:', lista_objetos[1])

# Etapa 4
# Remover item da lista
lista_objetos.pop(0)
#  lista_objetos.remove('mesa')
print(lista_objetos)

# Etapa 5
# Exibir tamanho da lista
print('\nA lista possui', len(lista_objetos), 'itens\n')

# Etapa 6
# Mostrar itens com laço for
for n, item in enumerate(lista_objetos, start=1):
    print(f'{n}- {item}')                       

# Etapa 7
# Verificar se "cadeira" esta na lista
if 'cadeira' in lista_objetos:
    print('\ncadeira esta na lista')
    lista_objetos.remove('cadeira')
    print('\no item "cadeira" foi removido da lista\n')
else:
    print('\ncadeira NÃO esta na lista')
    lista_objetos.append('cadeira')
    print('\no item "cadeira" foi adicionado da lista\n')


# Etapa 8
# Ordenar por ordem alfabetica
lista_objetos.sort()
print('\nitens ordenados:\n')
for n, item in enumerate(lista_objetos, start=1):
    print(f'{n}- {item}')


# Etapa 9
# Printar o primeiro e úlimo item
tamanho_lista = len(lista_objetos)
print('\nPrimeiro item:', lista_objetos[0])
print('\nÚltimo item:', lista_objetos[tamanho_lista - 1])

# Etapa 10
# Limpar toda a lista
lista_objetos.clear()
print('\nLista de objetos:')
print(lista_objetos)
