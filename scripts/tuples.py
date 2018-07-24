#create Tuples

t=1,2,3,4
print(type(t))#<class 'tuple'>
str="ganesh"
t=tuple(str)
print(type(t))#<class 'tuple'>
print(t)#('g', 'a', 'n', 'e', 's', 'h')

#unpack values from tuple
a,b,c,d,e,f=t
print(a)#g
print(c)#h