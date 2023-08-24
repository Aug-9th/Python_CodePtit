a = []
v = [0] * 30
cnt = [0] * 1005

def Try(i):
    if i == k + 1:
        for j in range(1, k + 1):
            print(a[v[j] - 1 ], end = ' ')
        print()
        return
    
    for j in range(v[i-1] + 1, n - k + i + 1):
        v[i] = j
        Try(i + 1)


n , k = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in c:
    if cnt[i] == 0:
        a.append(i)
        cnt[i] += 1
a.sort()
n = len(a)

v[0] = 0
Try(1)