# A set is an unordered collection with no duplicate elements

fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(fruits)#{'apple', 'orange', 'banana', 'pear'}


print('apple' in fruits) #True
print('mango' in fruits) #False

#create set from sequence

lettrs="abcdeabdcs"
ltr=set(lettrs)
print(ltr)#{'e', 'a', 'd', 'c', 'b', 's'}

a = set('abracadabra')
b = set('alacazam')
print(a-b)#{'b', 'r', 'd'}>>letters  in a but not in b
print(a | b)#{'a', 'r', 'l', 'z', 'c', 'b', 'd', 'm'} >>letters in a or b or in both
print(a & b)#{'a', 'c'} >> only common elements
print(a ^ b)#{'d', 'l', 'm', 'b', 'z', 'r'} letter in a and b but not in both