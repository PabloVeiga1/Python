s = int(input('S:'))
a = int(input('A:'))
b = int(input('B:'))

num = 0
i = 1
for i in range(a,b+1):
    i=str(i)
    if b < 100 and (int(i[0]) + int(i[len(i)-1])== s):
        num+=1
    elif (b >= 100 and b<=999) and (int(i[0]) + int(i[1])+ int(i[len(i)-1])== s):
        num+=1
    elif (b>999 and b <=9999) and (int(i[0]) + int(i[1])+ int(i[2])+int(i[3]))== s:
        num+=1
    if b == 10000  and (int(i[0]) + int(i[len(i)])+ int(i[2])+int(i[3]) + int(i[4]))== s:
        num+=1
print(num)


