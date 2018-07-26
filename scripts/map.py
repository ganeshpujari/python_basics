# map takes function as first argument,
# Sequencce as second argument,
# aply function on each element from sequence
# and returns a result iterable.


def cube(number):
    return number ** 3


cubes=map(cube,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(cubes)
print(type(cubes))


for element in cubes:
    print(element)