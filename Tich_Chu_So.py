t = int(input())
while t > 0:
    s = input()
    cnt = 1
    for i in s:
        if i != '0':
            cnt *= int(i)
    print(cnt)
    t -= 1