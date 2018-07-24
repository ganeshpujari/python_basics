#Dictionaries are key value mapping datastructure

d={'a':"A",'b':"B"}
print(d)#{'a': 'A', 'b': 'B'}

#Get values from d
print(d['a'])#A

#add element in d

d['c']="C"
print (d)#{'a': 'A', 'b': 'B', 'c': 'C'}
d.update({'d':"D"})
print (d)#{'a': 'A', 'b': 'B', 'c': 'C'}
#Get sorthed keys from d
print(sorted(d))#['a', 'b', 'c']

#Get keys from d
print(d.keys())#d_keys(['a', 'b', 'c'])

# Check is key exist or not in d
print('a' in d)#True

#Create dionary from key-value pairs
d=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)#{'sape': 4139, 'guido': 4127, 'jack': 4098}


#dict comprehensions:--Create dictory from element and some opration aplied in elements as its value
d={x: x**2 for x in (2, 4, 6)}
print(d)#{2: 4, 4: 16, 6: 36}


#Looping Techniques

for k,v in d.items():
    print(k,v)
#>>
'''
2 4
4 16
6 36'''
