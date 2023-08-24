pr = [1] * (105)
pr[0] = 0; pr[1] = 0
for i in range(2, 11):
    if pr[i] == 1:
        for j in range(i*i, 100, i):
            pr[j] = 0
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
def sum(n):
    res = 0
    while n > 0:
        res += (n % 10)
        n //= 10
    return res

t = int (input())
while t > 0:
    a, b = list(map(int, input().split()))
    print("YES" if pr[sum(gcd(a, b))] else "NO")
    t -= 1