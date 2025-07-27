palavras = (
    "estrela",
    "montanha",
    "livro",
    "computador",
    "janela",
    "oceano",
    "violao",
    "chave",
    "relampago",
    "pinguim",
    "misterio",
    "nuvem"
)

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='') #como aqui
    for letra in palavra:
        if letra in 'aeiou':
            print(letra,end=' ')#mais aqui

# Conclusoes finais: tenho que treinar a divisao de uma frase em mais de um for


