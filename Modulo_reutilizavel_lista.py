def criar_lista():
  return []

def mult_list(n, my_list):
  return my_list * n
  

def adicionar_elemento(lista, elemento):
  lista.append(elemento)

def adicionar_elemento_posicao(lista, elemento, pos):
  lista.insert(pos-1,elemento)

def remover_elemento(lista, elemento):
  if elemento in lista:
    lista.remove(elemento)
  else:
    print(f"{elemento} não encontrado na lista.")


def obter_elementos(lista):
  return lista


def limpar_lista(lista):
  lista.clear()



# testes:
# minha_lista = criar_lista()
# adicionar_elemento(minha_lista, 1)
# adicionar_elemento(minha_lista, 2)
# adicionar_elemento(minha_lista, 3)
# adicionar_elemento_posicao(minha_lista, 5, 1)

# print("Lista original:", obter_elementos(minha_lista))

# remover_elemento(minha_lista, 2)
# print("Lista após a remoção:", obter_elementos(minha_lista))

# limpar_lista(minha_lista)
# print("Lista após a limpeza:", obter_elementos(minha_lista))
