'''
Generators are a simple and powerful tool for creating iterators.
Generators looks like normal fuunction just replace return with yield.
__next__() method used to fetch elements from generator object.
Generator remember last fetch elements. So each __next__()call it return next element.
When no element in generator object it raise StopIterationException.


'''

def reverse_data(data):
    last_index=len(data)-1
    for index in range(last_index,-1,-1):
        yield data[index]


rev_data=reverse_data("ganesh")
print(next(rev_data))
print(next(rev_data))
print(next(rev_data))
print(next(rev_data))
print(next(rev_data))
print(next(rev_data))
# print(next(rev_data))  StopIteration

#Generator Expressions
'''
We can create generator with expresion.
simple replace [] with () in list comprahansions.
'''

gen_obj=(i**2 for i in range(5))
print(gen_obj.__next__())#0
print(gen_obj.__next__())#1
print(gen_obj.__next__())#4
print(gen_obj.__next__())#9
print(gen_obj.__next__())#16
# print(genObj.__next__())#StopIteration

gen_obj=(i**3 for i in range(5))

for data in gen_obj:
    print(data)