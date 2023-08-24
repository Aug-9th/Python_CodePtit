n = int(input());
a = list(map(int, input().split()))
x =[]

for i in range(0, n):
    if (len(x) > 0 and (x[-1] + a[i]) % 2 == 0):
        x.pop()
    else:
        x.append(a[i])
print(len(x))