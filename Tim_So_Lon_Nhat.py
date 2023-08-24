n = int(input())
while n > 0:
    s = input()
    tmp =""
    res = -1
    for i in range(0, len(s)) :
        if (s[i] >= '0' and s[i] <= '9'):
            tmp += s[i]
        else :
            if tmp != "" :
                res = max(res, int(tmp))
            tmp = ""
    if tmp != "":
        res = max(res, int(tmp))
    print(res)
    n-=1
    