import math
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for t in range(int(input())):
    s = input()
    check = 0
    for i in range(len(s)):
        if snt(i) == True and snt(int(s[i])) == False:
            check = 1
            break
        elif snt(i) == False and snt(int(s[i])) == True:
            check = 1
            break
    if check == 0:
        print('YES')
    else:
        print('NO')
