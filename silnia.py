from math import factorial

def silnia_iter(N):
    for i in range (1,N):
        N *= i
    return N

def silnia(n):
    if n < 0:
        raise ValueError("Silnia jest zdefiniowana tylko dla liczb nieujemnych.")
    if n == 0 or n == 1:  # warunek bazowy
        return 1
    return n * silnia(n - 1)  # wywołanie rekurencyjne

liczba = 5
print(f"Silnia {liczba} wynosi {silnia(liczba)}")

print(silnia_iter(5))