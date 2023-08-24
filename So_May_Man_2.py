t = int (input())

for i in range(t):
    n = input()
    check = True
    for i in n:
        if i != '4' and i != '7':
            check = False
            break
    
    if check:
        print("YES")
    else:
        print("NO")