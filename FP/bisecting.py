import bisect

lista = [1,2,3,4,5,6,7,4,33,2]

lusta = [1,2,2,3,4,4,5,6,7,33]

simplista = [0,1,2,3,4,5,6,7,8,9,10]

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n == 1 or n ==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def returnnum(list):
    return [x for x in list if x % 2 == 0]

