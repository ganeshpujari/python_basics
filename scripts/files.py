f=open('smpl.txt','r')
txt=f.read()#Print all content of a file
print(txt)
f.close()

f=open('smpl.txt','r')
line1=f.readline()
line2=f.readline()
print(line1)#Read the first line
print(line2)#read the second line
# f.close()

lines=f.readlines()#Return list of all lines
print(lines)
f.close()

fw=open('smpl2.txt','w+')
oldTxt=fw.read()
print(oldTxt)
fw.write("Thios is first line writen by developer ganesh")
print("PPPPPPPP")
print(fw.tell())#Returns cuttent file pointer possition