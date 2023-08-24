t = int(input())
def xuli():
    s = input()
    adu = ['0', '1', '2']
    for j in s:
        if(j not in adu):
            return "NO"
    return "YES"
        
for i in range(t):
    print(xuli())