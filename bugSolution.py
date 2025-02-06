def function(x):
    fib = [0, 1]
    if x <= 1:
        return fib[x]
    else:
        for i in range(2, x + 1):
            next_fib = fib[i - 1] + fib[i - 2]
            fib.append(next_fib)
        return fib[x]