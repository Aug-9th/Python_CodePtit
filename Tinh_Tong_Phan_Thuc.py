t =  int (input())
while t > 0:
    n = int (input())
    k = 1 if n % 2 == 1 else 2
    sum = float(0)
    for i in range(k, n+1, 2):
        sum += 1/i

    print('%.6f' %sum)
    t -= 1