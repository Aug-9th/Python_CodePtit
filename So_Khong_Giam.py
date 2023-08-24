t = int (input())
for i in range(t):
    n = input()
    check = True
    for i in range(1, len(n)):
        if int (n[i]) < int (n[i-1]):
            check = False
            break
 
    print("YES" if check == True else "NO")
