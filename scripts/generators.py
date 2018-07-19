'''
Generators are a simple and powerful tool for creating iterators.
Generators looks like normal fuunction just replace return with yield.
__next__() method used to fetch elements from generator object.
Generator remember last fetch elements. So each __next__()call it return next element.
When no element in generator object it raise StopIterationException.


'''

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]


rev=reverse("Ganesh")
print(type(rev))#<class 'generator'>
print(rev.__next__())#h
print(rev.__next__())#s
print(rev.__next__())#e
print(rev.__next__())#n
print(rev.__next__())#a
print(rev.__next__())#G
# print(rev.__next__())#StopIteration


#Generator Expressions
'''
We can create generator with expresion.
simple replace [] with () in list comprahansions.
'''

genObj=(i**2 for i in range(5))
print(genObj.__next__())#0
print(genObj.__next__())#1
print(genObj.__next__())#4
print(genObj.__next__())#9
print(genObj.__next__())#16
# print(genObj.__next__())#StopIteration