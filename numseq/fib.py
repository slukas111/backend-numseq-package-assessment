
def fib(n):
    """"returns the nth Fibonacci number"""
    old, new = 0, 1
    if n == 0:
        return 0
    for _ in range(n-1):
        old, new = new, old + new
    return new

#print(fibonacci(10))    

