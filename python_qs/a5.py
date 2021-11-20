N=int(input("Enter value of N: ")) #N numbers
l=list()
d=dict()
for i in range(N):
    l.append(int(input("Enter number {}: ".format(i+1))))
for i in l:
    b=bin(i).replace("0b","") 
    o=oct(i).replace("0o","")
    h=hex(i).replace("0x","") 
    d[i]=[b,o,h]
print("Below output is in the form of decimal:[binary,octal,hexadecimal]")
print(d)
