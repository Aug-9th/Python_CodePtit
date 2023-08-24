import math
def isPrime(n):
    if n < 2: 
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return True

def check(n):
    if not isPrime(int (n)) or not isPrime(int (n[::-1])):
        return False
    
    sum = 0
    for i in range(len(n)):
        if not isPrime(int (n[i])) :
            return False
        sum += int (n[i])
    return True if isPrime(sum)  else False

t = int (input())
while t > 0:
    n = input()
    print("Yes" if check(n) else "No")
    t-=1