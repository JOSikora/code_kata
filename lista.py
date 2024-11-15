from random import uniform

lista = []
lista.append(uniform(-1,1))
lista.append(uniform(-1,1))
lista.append(uniform(-1,1))
lista.append(uniform(-1,1))
lista.append(uniform(-1,1))

for i in range(len(lista)):
    print('lista['+str(i)+ ']: ', lista[i])
#   print(f'lista[{i}]: ', lista[i])

print('Lista zawiera', len(lista), 'elementow.')
print('Największy element listy ma indeks', lista.index(max(lista)),'i wartosc', max(lista))
