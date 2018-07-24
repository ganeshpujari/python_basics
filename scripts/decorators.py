# Decoratorr is use to add extra functionality to existing function.
# Decorator excutes befor actual function execution

def is_even_number(func):
    def check(no1,no2):
        if no1 % 2 == 0 and no2 % 2 ==0:
            return func(no1, no2)
    return check


@is_even_number
def sum(no1, no2):
    return no1+no2

add=sum(10,10)
print(add)#20

add=sum(10,7)
print(add)#None

#Class decorator example

class IsEvenNumbers(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        if args[0] % 2 == 0 and args[1] % 2 == 0:
            return self.func(*args)


@IsEvenNumbers
def sum(no1, no2):
    return no1+no2

add=sum(20,20)
print(add)#40

add=sum(31,20)
print(add)#None