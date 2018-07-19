#Scopes and Namespaces Example

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)#After local assignment: test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)#After nonlocal assignment: nonlocal spam
    do_global()
    print("After global assignment:", spam)#After global assignment: nonlocal spam

scope_test()
print("In global scope:", spam)#In global scope: global spam


#Class example

class MyClass():
    def __init__(self):
        print("This magic method invoked on object creations.")

    def my_func(self):
        print("This is class method")

my_class=MyClass()#Object creation
my_class.my_func()#method call

#Single Inheritance

class Base():
    def my_function(self):
        print("Base class Function")

class Derived(Base):
    def my_function(self):
        print("Derived Class method")

derived=Derived()
derived.my_function()#Derived Class method
base=Base()
base.my_function()#Base Class Function

#Multi-level Inheritance

class Base():
    def my_function(self):
        print("Base class Function")

class Derived(Base):
    def my_function(self):
        print("Derived Class method")

class Child(Derived):
    def my_function(self):
        print("Chield Class method")


derived=Derived()
derived.my_function()#Derived Class method
base=Base()
base.my_function()#Base Class Function
child=Child()
child.my_function()#Chield Class method

#Multiple Inheritance

class Base():
    def my_function(self):
        print("Base class Function")

class Derived(Base):
    def my_function(self):
        print("Derived Class method")

class Chield(Derived,Base):
    def my_function(self):
        print("Chield Class method")


d=Derived()
derived.my_function()#Derived Class method
base=Base()
base.my_function()#Base Class Function
child=Chield()
child.my_function()#Chield Class method