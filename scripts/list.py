#List inbuilt functions
lst=[4,5]
list=[1,2]
print (list)#[1, 2]
list.append(3)
print (list)#[1, 2, 3]
list.extend(lst)
print (list)#[1, 2, 3, 4, 5]
list.insert(0,10)
print (list)#[10, 1, 2, 3, 4, 5]
list.remove(10)
print (list)#[1, 2, 3, 4, 5]
list.pop()
print (list)#[1, 2, 3, 4]
list.clear()
print (list)#[]
list=[1,2]
print (len(list))#2
print(list.count(2))#1
list=[5, 4, 3, 1 , 2]
list.sort(reverse=False)
print(list)#[1, 2, 3, 4, 5]
list.reverse()
print(list)#[5, 4, 3, 2, 1]


#List as a stack
list=[1,2,3,4,5]
print(list)#[1, 2, 3, 4, 5]
list.append(6)
print(list)#[1, 2, 3, 4, 5, 6]
list.pop()
print(list)#[1, 2, 3, 4, 5]


#List as a Queue
from collections import deque
list=[1,2,3,4,5]
queue = deque(list)
print(queue)#deque([1, 2, 3, 4, 5])
queue.append(6)
print(queue)#deque([1, 2, 3, 4, 5, 6])
queue.popleft()
print(queue)#deque([2, 3, 4, 5, 6])


# List Comprehensions
'''
resultant list from sequences
'''

list=[1,2,3,4,5]
square_list=[i**2 for i in list]
print(square_list)#[1, 4, 9, 16, 25]

vec = [[1,2,3], [4,5,6], [7,8,9]]
new_list=[num for elem in vec for num in elem]
print(new_list)#[1, 2, 3, 4, 5, 6, 7, 8, 9]


#del statment
list=[1,2,3,4,5]
print(list)#[1, 2, 3, 4, 5]
del(list[0])
print(list)#[2, 3, 4, 5]