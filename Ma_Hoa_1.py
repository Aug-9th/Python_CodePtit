t = int (input())
while t > 0:
    s = input()
    cnt = 1
    s = s + "."
    for i in range (len(s)-1):
        if(s[i] == s[i+1]):
            cnt+=1
        else:
            print(f'{cnt}{s[i]}', end = '')
            cnt = 1
    print()
    t -= 1