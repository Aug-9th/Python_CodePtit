import math

primes = []
def snt(n):
    check = [True for i in range(n + 1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if check[i] == True:
            primes.append(i)
            for i in range(i * i, n + 1, i):
                check[i] = False
sum = 0
snt(2000000)
for t in range(int(input())):
    n = int(input())
    for i in primes:
        if i > n:
            break
        while n % i == 0:
            sum += i
            n /= i
print(sum)