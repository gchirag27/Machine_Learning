a=input("First string") #string a
b=input("Second string") #string b
d=0 #number of elements deleted
l1=list(set(a.replace(" ",""))) #removing all common elements in a
l2=list(set(b.replace(" ",""))) #removing all commom elements in b
for i in l1:
    if i in l2:
        d+=abs(a.count(i)-b.count(i))
    else:
        d+=a.count(i)
for i in l2:
    if i not in l1:
        d+=b.count(i)
print("Minimum number of characters deleted:",d)