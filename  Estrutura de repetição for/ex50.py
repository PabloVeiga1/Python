soma = 0
contp = 0
conti=0
for i in range(1,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        contp += 1
        soma+=n
    else:
        conti+=1

if contp >0:
    print(f'Foram digitados {contp} numeros pares, e a soma deles eh igual a {soma}')
elif contp ==0:
    print(f'Foram digitados apenas numeros impares.')