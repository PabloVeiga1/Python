from math import radians,sin,cos,tan
ang = float(input('Digite um angulo:'))
sen = sin(radians(ang))
print('O seno de {} eh igual a {:.2f}'.format(ang,sen))
cos = cos(radians(ang))
print('O coseno de {} eh igual a {:.2f}'.format(ang,cos))
tan = tan(radians(ang))
print('A tangente de {} eh igual a {:.2f}'.format(ang,tan))
