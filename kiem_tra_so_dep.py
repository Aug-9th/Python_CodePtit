for i in range(int(input())):
    s = input()
    check = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != s[0]:
            check = 1
            break
        elif i % 2 == 1 and s[i] != s[1]:
            check = 1
            break
    if check == 0:
        print('YES')
    else:
        print('NO')