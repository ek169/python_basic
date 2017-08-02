def modified_fib(first, second, nth):
    for i in range(0, nth):
        fib = first + second**2
        print(fib)
        first = second
        second = fib

modified_fib(0, 1, 5)