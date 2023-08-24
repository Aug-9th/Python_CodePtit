s = "0123456789ABCDEF"
t = int(input())
while t > 0:
    b = int(input())
    a = int(input(), 2)
    res =""
    while a > 0:
        res += s[int (a % b)]
        a //= b
    print(res[::-1])
    t -= 1