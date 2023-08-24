import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
for t in range(int(input())):
    n = input()
    sum = 0
    check = 0
    for i in range(len(n)):
        sum += int(n[i])
        if i % 2 == 0 and int(n[i]) % 2 == 1:
            check = 1
            break
        elif i % 2 == 1 and int(n[i]) % 2 == 0:
            check = 1
            break
    if snt(sum) == False:
        check = 1
    if check == 1:
        print('NO')
    else:
        print('YES')
