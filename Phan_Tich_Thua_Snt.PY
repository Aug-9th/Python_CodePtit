import math
t = int (input())
while t > 0:
    n = int (input())
    
    res = ""
    res += "1 * "

    for i in range(2, int (math.sqrt(n))):
        cnt = 0
        while(n % i == 0):
            cnt += 1
            n /= i
        if cnt > 0:
            res += f'{i}^{cnt} * '
    if (n > 1):
        res += f'{int (n)}^1 * '
    print(res[:len(res)-2])
    t -= 1