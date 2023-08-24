t = int (input())
while t > 0:
    a = input()
    b = a[::-1]
    check = 1
    
    for i in range(1, len(a)):
        if(abs( ord(a[i]) - ord(a[i-1])) != abs(ord(b[i]) - ord(b[i-1]))) :
            check = 0
            break
    print("YES" if check == 1 else "NO")

    t-=1