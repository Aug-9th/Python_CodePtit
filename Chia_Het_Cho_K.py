a, k, n = list(map(int, input().split()))

b1 = (int(a / k) + 1) * k - a
b2 = int(n / k) * k - a

if b1 <= b2:
    for i in range(b1, b2 + 1, k):
        print(i, end=' ')
else:
    print(-1)