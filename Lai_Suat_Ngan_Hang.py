import math
t = int (input())
for i in range(t):

    n, x, m = list(map(float, input().split()))
    x = x / 100
    res = float (math.log(m/n, (1 + x)))
    if res == int(res):
        print(int (res))
    else:
        print(int (res + 1))