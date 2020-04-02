"""square"""
def square(n):
    return n*n

"""triangle(n)` : Returns the nth term of the numbers
 that can be arranged in triangular geometric shape"""
def triangle(n):
    for i in range(1, n + 1):   
        print("n = {0}, triangle = {1}".format(i, (i ** 2 + i)//2))

"""cube"""
def cube(n):
    return n**3