a = int(input('Czesc! Podaj liczbe a: '))
b = int(input('A teraz druga liczbe b: '))

r = a%b

if r == 0:
    print('liczba a jest podzielna przez b')
else: print(f'reszta z dzielenia a przez b wynosi {r}')