def search(lista, n, x):
    for i in range(0, n):
        if lista[i] == x:
            return i
    return -1
