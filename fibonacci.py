def fibonacci(n,f1,f2):
    i = 0
    print(f1, end= ' ')
    print(f2, end = ' ')
    while i < n - 1:
        f3 = f1 + f2
        print(f3, end=' ')
        f1 = f2
        f2 = f3
        i += 1
fibonacci(6,1,1)