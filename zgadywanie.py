import random

a = random.randint(0,10)
x = int(input('Zgadnij o jakiej liczbie mysle od 1 do 10: '))
licznik = 1
while x!=a:
    if x > a:
        print('za duzo')
        x = int(input('Zgaduj dalej: '))
        licznik += 1
    else:
        print('za malo')
        x = int(input('Zgaduj dalej: '))
        licznik += 1

print('zgadles! po', licznik, 'probach')
