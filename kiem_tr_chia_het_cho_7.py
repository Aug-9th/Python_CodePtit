def sum(tmp):
    return tmp + int(str(tmp)[::-1])
for i in range(int(input())):
    s = int(input())
    n = 1000
    check = 0
    while n > 0:
        if s % 7 == 0:
            print(s)
            check = 1
            break
        s = sum(s)
        n -= 1
    if check == 0:
        print(-1)
