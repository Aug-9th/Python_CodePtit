t = int (input())
while t > 0:
    p, q = list(map(str, input().split()))
    s = input().split()
    if(len(s) > 1):
        a, b = s[0], s[1]
    else:
        a = s[0]
        b = input()
    r1, r2 = 0, 0
    r1 = int (a.replace(p, q)) + int (b.replace(p, q))
    r2 = int (a.replace(q, p)) + int (b.replace(q, p))
    
    print(min(r1, r2), max(r1, r2))
    t -= 1