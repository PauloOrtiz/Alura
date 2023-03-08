A, B = map(float, input().split())

if A == 0 and B == 0:
    Media = 0
elif A == 0:
    Media =  B / 2
elif B == 0:
    Media = A / 2
else:
    Media = (A + B) / 2

if Media >= 7:
    print('Aprovado')
elif Media >= 4:
    print('Recuperacao')
else:
    print('Reprovado')