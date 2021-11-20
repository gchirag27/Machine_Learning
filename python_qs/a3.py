N=int(input("Enter number of steps: ")) #number of steps
a="|    |"
b="------"
for i in range(N*2+1):
    if(i%2==0):
        print(a)
    else:
        print(b)
