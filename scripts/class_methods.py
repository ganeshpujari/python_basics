#Class method>> Instance method, Class method, Static method

class MethodTypes(object):

    def __init__(self):
        print("this method called on "
              "object creation.")

    def instance_method(self):
        print("This method called by object only,"
              " Not even with class name.")

    @classmethod
    def class_method(cls):
        print("This method called with "
              "class name as well as class instance")

    @staticmethod
    def static_method():
        print("we can call it by class name "
              "or class instance")


method_types=MethodTypes()
method_types.instance_method()
method_types.class_method()
MethodTypes.class_method()
MethodTypes.static_method()
method_types.static_method()

#Singleton Class:- Restrict to only one copy of the instance
class SingletonClass(object):
    _instance = None
    def __new__(cls,*args, **kwargs):
        if not isinstance(cls._instance,cls):
            cls._instance=object.__new__(cls,*args, **kwargs)
        return cls._instance

singleton_class_obj1=SingletonClass()
singleton_class_obj2=SingletonClass()
print(id(singleton_class_obj1))
print(id(singleton_class_obj2))

