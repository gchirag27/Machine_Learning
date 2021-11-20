n=int(input("Order of matrix: ")) #order of matrix
r=list() #rows of matrix
m=list() #input matrix
sd1=0 #sum of first diagonal  
sd2=0 #sum of second diagonal
for i in range(1,n+1):
	r=[]
	for j in range(1,n+1):
		r.append(int(input("Enter element in row {i} and column {j}".format(i=i,j=j))))
	m.append(r)
for i in range(n):
	for j in range(n):
		print()
		if(i==j):
			sd1+=m[i][j]
		if(i==(n-j-1)):
			sd2+=m[i][j]
print("Difference in diagnols is:",abs(sd1-sd2))