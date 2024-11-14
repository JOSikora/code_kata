N = int(input('sprawdze czy dana liczba jest doskonala: '))
sum = 0

for n in range(1,N):
    if N%n == 0:
        sum += n

if sum == N:
    print('TAK')
else: print('NIE')