def fib():
    x, y = 1, 2	
    while True:
        yield x
        x, y = y, x + y
