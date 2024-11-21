from math import factorial
#choinka

n = int(input('podaj wielkosc choinki: '))
for r in range(1,n+1):
    print('*'*r)




#trojkat pascala do sciany

x = int(input('Podaj wielkosc trojkata Pascala: '))

for i in range(x+1):
    lista = []
    for j in range(i+1):
        lista.append(str(int(factorial(i)/(factorial(j)*factorial(i-j)))))
    print(' '.join(lista))

# ladny trojkat rownoraminny
a = int(input('Podaj wielkość trójkąta Pascala: '))

for i in range(a + 1):
    row = []
    for j in range(i + 1):
        row.append(str(int(factorial(i) / (factorial(j) * factorial(i - j)))))

    # Wycentrowanie wiersza
    print(' ' * (a - i), ' '.join(row))
