n = int(input())
while n > 0:
    s = input()
    tmp =""
    res = 10 ** 18
    for i in range(0, len(s)) :
        if (s[i] >= '0' and s[i] <= '9'):
            tmp += s[i]
        else :
            if tmp != "" :
                res = min(res, int(tmp))
            tmp = ""
    print(res)
    n-=1
