# Iterator
'''
iter() method return iterable object from any sequence.
StopIteration exception raised when no more element in object.
'''

name="Ganesh"
name_obj=iter(name)
print(next(name_obj))# G
print(next(name_obj))# a
print(next(name_obj))# n
print(next(name_obj))# e
print(next(name_obj))# s
print(next(name_obj))# h
# print(next(name_obj))#StopIteration

name="Ganesh"
name_obj=iter(name)

for nm in name_obj:
    print(nm)

# user defined interator

class CharatorsFromData():

    def __init__(self,data):
        self._index=0
        self._data=data

    def __iter__(self):
        return self

    def __next__(self):
        if self._index>=len(self._data):
            raise StopIteration("No more element")
        ret_index=self._index
        self._index+=1
        return self._data[ret_index]


charators_from_data=CharatorsFromData("Pujari")
for ch in charators_from_data:
    print(ch)
# print(next(charators_from_data))#StopIteration