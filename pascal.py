from math import factorial
#choinka

n = int(input('podaj wielkosc choinki: '))
for r in range(1,n+1):
    print('*'*r)




x = int(input('Podaj wielkosc trojkata Pascala: '))

for i in range(x+1):
    list = []
    for j in range(i+1):
        list.append(str(int(factorial(i)/(factorial(j)*factorial(i-j)))))
    print(' '.join(list))