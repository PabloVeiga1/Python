lista =['a', 'b', 'a', 'c', 'b', 'd']
novaLista = []
for i in lista:
    if i not in novaLista:
        novaLista.append(i)
print(novaLista)