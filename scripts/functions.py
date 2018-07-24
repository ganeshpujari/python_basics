

def default_argument_value(arg1,arg2=20):
    '''Default Argument Values Example'''
    sum=arg1 + arg2
    return sum

print("default_argument_value")
summation=default_argument_value(10,10)
print(summation)#>>20
summation=default_argument_value(10)
print(summation)#>>30


def keyword_argument(arg1=10,arg2=20,arg3=30):
    '''Keyword Arguments Example'''
    print(arg1)

print("Keyword Arguments")
keyword_argument()#>>10
keyword_argument(arg2=50)#>>10
keyword_argument(arg1=50)#>>50
keyword_argument(arg1=50,arg2=60)#>>50

def multiple_argument_in_single_variable(*args):
    '''passing multiple argument to function dynamically'''
    for arg in args:
        print(arg)




print("multiple_argument_in_single_variable")
multiple_argument_in_single_variable(1)#>>1
multiple_argument_in_single_variable(1,2)#1,2
multiple_argument_in_single_variable()#

def key_value_as_arguments(**kwargs):
    '''passing multiple key-value argument to function dynamically'''
    print(kwargs)

print("key_value_as_arguments")
key_value_as_arguments(a=1)#{'a': 1}
key_value_as_arguments(a=1,b=2)#{'a': 1, 'b': 2}

def multiple_argument_in_single_variable_with_unpack(*args):

    '''to Unpack arguments * is used'''
    print(*args)

print("multiple_argument_in_single_variable_with_unpack")
multiple_argument_in_single_variable(1)#>>1
multiple_argument_in_single_variable(1,2)#1,2
multiple_argument_in_single_variable()#



# Lambda Expressions: This is simple anonymous  function restricated to anly single expressions.

sum=lambda a,b:a + b
add=sum(10,20)
print(add)#30


#annotations
def annotations(arg1:str,arg2)->str:
    return arg1

retData=annotations(10,20)
print(type(retData))
