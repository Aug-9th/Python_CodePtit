import math
def ct(n):
    if n < 2:
        return False;
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for t in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if ct(sum):
        print('YES')
    else:
        print('NO')
