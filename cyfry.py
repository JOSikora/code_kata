x= int(input('podaj liczbe: '))

sum_digits = sum(int(digit) for digit in str(x) )

print('Ta liczba ma '+str(len(str(x)))+' cyfry a ich suma to: ', sum_digits)