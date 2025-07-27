"""
    listaP = []
    for i in range(5):
    p = input(f'Palavra {i+1}:')
    listaP.append(p)
print(listaP)
"""
palindromos = []
for i in range(5):
    palavra = input('Palavra: ')
    palavra = palavra.replace(" ","")
    if palavra.upper() == palavra[::-1].upper():
        palindromos.append(palavra.upper())
print(palindromos)




