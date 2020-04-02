
"""
Within the fib module, define a function `fib(n)` that returns the nth Fibonacci
 number.  The first 10 terms of the Fibonacci sequence are 
`[0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...]`"""
def fibonacci(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for _ in range(n-1):
        old, new = new, old + new
    return new

#print(fibonacci(10))    

