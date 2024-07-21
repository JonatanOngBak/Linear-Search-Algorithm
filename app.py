from search import search

lista = [2, 3, 4, 10, 40]
n = len(lista)
x = 40

result = search(lista, n, x)
if(result == -1):
    print("Elemento não está presente na lista")
else:
    print("Elemento está presente no índice ", result)
