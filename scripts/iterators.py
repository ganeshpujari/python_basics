#for loop internali calles iter() method, This will return itarable object then we can fetch element from object with the help of __next__().

s="Ganesh"
iObj=iter(s)
print(type(iObj))#<class 'str_iterator'>
print(iObj.__next__())#G
print(iObj.__next__())#a
print(iObj.__next__())#n
print(iObj.__next__())#e
print(iObj.__next__())#s
print(iObj.__next__())#h
# print(iObj.__next__())#StopIteration

#User defined class as interator

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rObj=Reverse("ganesh")
iter(rObj)
for data in rObj:
    print(data)