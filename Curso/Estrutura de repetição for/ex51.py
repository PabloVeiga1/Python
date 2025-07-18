print('='* 30)
print('10 TERMOS DE UMA PA')
print('='* 30)

p1 = int(input('Primeiro termo: '))
r = int(input('Razao: '))
for x in range(p1,11,r):
    print(x,end=' -> ')
print('Acabou',end=' ')
