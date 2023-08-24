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
    tmp = n[-4:]
    if snt(int(tmp)):
        print('YES')
    else:
        print('NO')
