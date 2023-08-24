def check(s):
    if len(s) % 2 == 1:
        return False
    if s != s[::-1]:
        return False
    for i in s:
        if int(i) % 2 != 0:
            return False
    return True

t = int (input())
while t > 0:
    n = int (input())
    for i in range(22, n, 2):
        if check(str (i)):
            print(i, end = ' ')
    print()
    t -= 1