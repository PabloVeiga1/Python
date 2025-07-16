'''
15. Codificador Simples
Crie um pequeno “código secreto”:

Peça ao usuário uma frase.

Troque cada letra por seu caractere seguinte no alfabeto (ex.: “a” → “b”, “b” → “c”… “z” → “a”). Ignore espaços.
'''
frase = input('Digite uma frase: ')
final = ''

for letra in frase:
    if letra.isalpha():
        if letra.islower():
            # letra minúscula
            nova = chr((ord(letra) - 97 + 1) % 26 + 97)
        else:
            # letra maiúscula
            nova = chr((ord(letra) - 65 + 1) % 26 + 65)
        final += nova
    else:
        final += letra

print(final)
