lista = [5, 2, 8, 1]

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)