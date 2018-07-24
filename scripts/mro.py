

class ClassOne:

    def func(self):
        print("This is classOne")


class ClassTwo():

    def func(self):
        print("This is classTwo")

class ClassThree(ClassOne, ClassTwo):

    def function(self):
        print("This is class Three")

class_three=ClassThree()
class_three.func()#This is classOne

class ClassOne():

    def func(self):
        print("This is classOne")


class ClassTwo(object):

    def func(self):
        print("This is classTwo")

class ClassThree(ClassTwo, ClassOne):

    def function(self):
        print("This is class Three")

class_three=ClassThree()
class_three.func()#This is classTwo