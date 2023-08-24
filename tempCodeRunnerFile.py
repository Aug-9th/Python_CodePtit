def check(index, s):
    for i in range(index +1):
        if(s[i] > s[i+1]):
            return False
    for i in range(index, len(s) - 2):
        if(s[i] < s[i+1]):
            return False
    return True
def xuli():
    s = input()
    n = len(s)
    st = set(s)
    if(len(st) < 3):
        return "NO"
    for i in range(n):
        if(check(i,s) == True):
            return "YES"
    return "NO"

t = int(input())
for i in range(t):
    print(xuli())