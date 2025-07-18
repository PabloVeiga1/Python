t = input('Digite algo: ')
t_f = t.replace(' ', '').upper().strip()

if t_f == t_f[::-1]:
    print(f'"{t}" é um Palíndromo')
else:
    print(f'"{t}" não é um Palíndromo')
