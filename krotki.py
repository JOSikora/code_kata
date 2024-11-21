pocket = ('pen', 'pencil', 'keys')

print('zawartosc portfela:', pocket)

if "keys" in pocket:
    print("Yes, 'keys' are in the pocket")
else: print('NO!')


print('Liczba elementow w portfelu:',len(pocket))
print('Ostatnio dodano do portfela:', pocket[-2:])

add = ('coins',)

pocket += add
print(pocket)
wallet = ('money', 'cards')
pocket += (wallet),

print(pocket)


