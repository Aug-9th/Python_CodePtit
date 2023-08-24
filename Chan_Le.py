
def check(s):
    sum = int(s[0])
    c = True
    for i in range(1, len(s)):
        if abs(int(s[i-1]) - int (s[i])) != 2 :
            c = False
            break
        sum += int (s[i])
    if c == True and sum % 10 == 0:
        return True
    else:
        return False



t = int (input())
while t >0:
    s = input()
    print("YES" if check(s) else "NO")
    t -= 1