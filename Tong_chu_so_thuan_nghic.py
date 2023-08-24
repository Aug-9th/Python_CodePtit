def ct(tmp):
    return str(tmp) == str(tmp)[::-1]

for i in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if ct(sum) and len(str(sum)) > 1:
        print('YES')
    else:
        print('NO')
