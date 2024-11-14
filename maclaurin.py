from math import factorial, exp

N = 5
x = 2
sum = 0

for n in range(0,N):
    sum += x**n / factorial(n)
print(sum)

print(exp(x))