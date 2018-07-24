

#Internet Access
from urllib.request import urlopen
with urlopen('http://google.com') as response:
     for line in response:
        print(line)


#Dates and Times
from datetime import date
now = date.today()
print(now)
dt=now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(dt)
birthday = date(1964, 7, 31)
age = now - birthday
age.days
14368



#Data Compression
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
print(t)#b'x\x9c+\xcf,I\xceP(\xcf\xc8\x04\x92\x19\x89\xc5PV9H4\x15\xc8+\xca,.Q(O\x04\xf2\x00D?\x0f\x89'
print(len(t))#37
zlib.decompress(t)
zlib.crc32(s)
print(len(t))
print(t)



#Performance Measurement
'''
Performance Measurement helpfull to mesure which solution is better for the same task.

'''

from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())#0.06702475899999993
print(Timer('a,b = b,a', 'a=1; b=2').timeit())#0.07576591700000002
