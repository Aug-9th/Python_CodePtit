
for i in range(int(input())):
    n = input()
    sum = 0
    mul = 1
    for i in range(len(n)):
        if i % 2 == 0:
            if int(n[i]) != 0:
                mul *= int(n[i])
        else:
            sum += int(n[i])
    print(mul, sum)
