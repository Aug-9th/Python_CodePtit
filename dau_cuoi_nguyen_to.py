import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for t in range(int(input())):
    n = input()
    tmp1 = n[:3]
    tmp2 = n[-3:]
    if snt(int(tmp1)) and snt(int(tmp2)):
        print('YES')
    else:
        print('NO')