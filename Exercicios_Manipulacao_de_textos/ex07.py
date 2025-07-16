texto = input('Insira uma frase: ')
palavra = input('Insira uma palavra: ')
t_s_e = texto.replace(' ', '')
if palavra in texto:
    print(f'"{palavra}" esta presente no texto, a partir do {t_s_e.find(palavra)+1}° caractere')