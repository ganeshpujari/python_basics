#Try except
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
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
    print("if exceptione comes or not this block garanty to exicute")