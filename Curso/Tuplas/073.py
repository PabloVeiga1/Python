times_brasileirao = (
    "Flamengo","Palmeiras","Botafogo","Atlético-MG",
    "Athletico-PR","Grêmio","Bragantino","Fortaleza","Bahia","São Paulo",
    "Internacional","Cruzeiro","Juventude","Corinthians","Vasco",
    "Cuiabá","Atlético-GO","Criciúma","Vitória","Fluminense"
)
print(f'Os 5 primeiros colocados foram: {times_brasileirao[:5]}')
print(f'Os ultimos 4 colocados da tabela foram: {times_brasileirao[-4:]} ')
print(f'Times em ordem alfabetica: {sorted(times_brasileirao)}')
print(f'O time do Corintias encontra-se na posicao: {times_brasileirao.index("Corinthians")+1}')
