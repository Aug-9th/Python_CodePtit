import math
l, r = list(map(int, input().split()))
r = r + 1
for i in range(l, r):
    for j in range(i+1, r):
        for k in range(j+1, r):
            if(math.gcd(i, j) == 1 and math.gcd(i, k) == 1 and math.gcd(j, k) == 1):
                print(f'({i}, {j}, {k})');