import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for i in range(int(input())):
    n = input()
    cnt = 0
    if snt(len(n)):
        for i in n:
            if snt(int(i)):
                cnt += 1
        if cnt > len(n) - cnt:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')