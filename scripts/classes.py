#Scopes and Namespaces Example

def scope_demonstration():

    def local():
        var = "I am local"

    def non_local():
        nonlocal var
        var = "I am nonlocal "

    def i_am_global():
        global var
        var = "I am global"

    var = "I am first"
    local()
    print("After local assignment:", var)#After local assignment: I am first
    non_local()
    print("After nonlocal assignment:", var)#After nonlocal assignment: I am nonlocal
    i_am_global()
    print("After global assignment:", var)#After global assignment: I am nonlocal

scope_demonstration()
print("In global scope:", var)#In global scope: I am global


#Class example

class MyClass():
    def __init__(self):
        print("This is same as constreuctor ")

    def func(self):
        print("This is member function")

my_class=MyClass()#Object creation
my_class.func()#method call

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