# Reduce combine the result.
# function as first argument
# sequence as second argument
# initial is opthion third parameter

from functools import reduce
result=reduce(lambda number1, number2 : number1 + number2, [1, 2, 3, 4, 5 ])
print(result)