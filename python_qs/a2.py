A=[1,23,456,7890] 
N=len(A) 
s=0
for i in A:
    s+=i%10
digit=s%10
print(s)
if(digit==0):
    print("Divisible by 10")
else:
    print("Not divisible by 10")