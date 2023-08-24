import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
t = int(input())
while t > 0:
    n = int(input())
    tmp = n
    m, csc2 = 0, 0
    while tmp > 0:
        csc = tmp % 10
        m = m * 10 + csc
        tmp = tmp // 10
    if gcd(m, n) == 1:
        print('YES')
    else:
        print('NO')
    t -= 1