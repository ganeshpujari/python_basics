#Try except
class Class1(Exception):
    pass

class Class2(Class1):
    pass

class Class3(Class2):
    pass

for cls in [Class1, Class2, Class3]:
    try:
        raise cls()
    except Class1:
        print("D")
    except Class2:
        print("C")
    except Class3:
        print("B")


#Try except Else>> when exception comes control goes in except else iit goes in else block.

try:
    10/10
except ZeroDivisionError:
    print("can't divid by zero")
else:
    print("working well")


#. Raising Exceptions

try:
    if 2 < 3:
        raise ValueError("First number should not small")
except ValueError as e:
    print(e)

#User defined Exceptions

class SmallNumberException(Exception):
    pass


try:
    if 2 < 3:
        raise SmallNumberException("First number should not small")
except SmallNumberException as e:
    print(e)


#Try except finally

try:
    1/0
except ZeroDivisionError:
    print("Exceptions")
finally:
    print("if exception comes or not this block guaranty to execute")