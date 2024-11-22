

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(6))

def fibsum(n):
    suma = 0
    for i in range(1, n+1):
        suma += fib(i)
    return suma

print(fibsum(6))