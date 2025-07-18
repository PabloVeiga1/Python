n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))

media = (n1 + n2)/2
media_passar = 6.0

if media >= media_passar:
    print(f'Tirando {n1} e {n2}, a media do aluno eh {media} e ele esta APROVADO!')
elif media < media_passar:
    print(f'Tirando {n1} e {n2}, a media do aluno eh {media} e ele esta de RECUPERACAO!')