a = int(input(''))
b = int(input(''))
c = int(input(''))
d = int(input(''))

num = [a,b,c,d]

maior = max(num)
menor = min(num)

num.remove(maior)
num.remove(menor)

soma = num[0] + num [1]
dif = (maior + menor)-soma
if dif < 0:
    dif = (maior + num[0])-(menor + num[1])
print(dif)

