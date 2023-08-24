a = []; 

def check(n):
    for i in n:
        if int(i) % 2 == 1:
            return False
    return True

n = 2
while n <= 888:
    num = str(n)
    if check(num):
        a.append(num + num[::-1])
    n += 2

t = int (input())
while t > 0:
    n = input()
    for i in a:
        if int(i) >= int(n):
            break
        print(i, end = ' ')
    print()
    t-=1
