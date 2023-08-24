t = int(input())
while t > 0:
    s = input()
    if len(s) % 2 == 0 or s[0] == s[1]:
        print('NO')
    else:
        tmp = s[0]
        for i in range(2, len(s), 2):
            if s[0] != s[i]:
                print('NO')
                break
        print('YES')
    t -= 1
