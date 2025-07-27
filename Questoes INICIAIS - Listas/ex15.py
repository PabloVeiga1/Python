lista = []
for i in range(5):
    n = int(input('N: '))
    lista.append(n)
novaLista = sorted(lista)
if lista == novaLista:
    print("Sim")
else:
    print("Nao")

