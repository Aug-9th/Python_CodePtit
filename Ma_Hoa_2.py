P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while(1):
    x = input()
    if x == "0":
        break
    k, s = x.split()
    k = int (k)
    res = ""
    for i in range(0, len(s)):
        res += P[((P.find(s[i])) + k) % 28]
    print(res[::-1])



