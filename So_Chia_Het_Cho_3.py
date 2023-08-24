t =int(input())
while t > 0:
    s = input()
    cnt = 0
    for i in s:
        cnt += int(i)
    if cnt % 3 == 0:
        print('YES')
    else:
        print('NO')
    t -= 1