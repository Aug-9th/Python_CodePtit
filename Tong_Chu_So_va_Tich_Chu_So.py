t = int(input())
while t > 0:
    s = input()
    sum, mul = 0, 1
    tmp = 0
    n = len(s)
    for i in range(0, n, 1):
        if i % 2 == 0:
            sum += int(s[i])
        else:
            if s[i] == '0':
                tmp += 1
            else:
                mul *= int(s[i])
    print(sum, end = ' ')
    if tmp == n // 2:
        print(0)
    else:
        print(mul)
    t -= 1

