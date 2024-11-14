
print('To są wszystkie liczby Catalana mniejsze od miliona')

c = 1
par = 0
npar = 1
print(c)
for n in range(1,100):
    if c>1000000:
        break
    else:
        if c%2 == 0:
            par += 1
        else: npar += 1
        print(c)
        c = c*(4*n +2)/(n+2)


print('Wsrod nich jest', npar, 'nieparzystych i ', par, 'parzystych.')

