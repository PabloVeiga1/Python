times_brasileirao = (
    'Vitória','Corinthians','Atlético-MG',
    'Cuiabá','Bahia','Fluminense',
    'Bragantino','São Paulo','Cruzeiro',
    'Grêmio','Coritiba','Juventude','Vasco','Internacional',
    'Santos','Palmeiras','Botafogo','Fortaleza','Athletico-PR',
    'Flamengo'
)


print(f'Lista dos times do Brasileirao: {times_brasileirao}')
print(f'Os 5 primeiros sao: {times_brasileirao[:5]}')
print(f'Os 4 ultimos sao: {times_brasileirao[-4:]}')
print(f'Times em ordem alfabetica: {sorted(times_brasileirao)}')
print(f'O flamengo esta na {sorted(times_brasileirao).index('Flamengo')+1} posicao')