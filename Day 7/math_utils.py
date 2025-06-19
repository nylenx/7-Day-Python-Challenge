def add(*args)->float:
    return sum(args)

def multiply(*args)->float:
    mul = 1
    for el in args:
        mul *=el
    return mul

def factorial(num:int)->int:
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)