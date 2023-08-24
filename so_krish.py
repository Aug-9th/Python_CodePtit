def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
for i in range(int(input())):
    s = input()
    sum = 0
    for i in s:
        sum += factorial(int(i))
    print('Yes' if s == sum else 'No')