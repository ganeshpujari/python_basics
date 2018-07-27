# Reduce combine the result.
# function as first argument
# sequence as second argument
# initial is opthion third parameter

from functools import reduce
result=reduce(lambda number1, number2 : number1 + number2, [1, 2, 3, 4, 5 ])
print(result)

def addition(number1, number2):
    return number1 + number2

result=reduce(addition,[10, 20, 30, 40 , 50, 60, 70, 80, 90, 100])
print(result)