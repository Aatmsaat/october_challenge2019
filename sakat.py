#practice mode example using brute force for visualizing patterns
#function for counting odd numbers in 2-D
def oddcount(a,n,m):
	c=0
	for i in range(n):
		for j in range(m):
			if a[i][j]%2!=0:
				c+=1
	return c
t=int(input())
for _ in range(t):
	n,m,q=list(map(int,input().split()))
	#Making 2-D array with the given dimensions n->rows 
	#and m-> columns initializing them zero
	a=[0]*n
	for i in range(n):
		a[i]=[0]*m
	print(a)
	while q:
		q-=1
		r,c=list(map(int,input().split()))
		for i in range(m):
			a[r-1][i]+=1
		for i in range(n):
			a[i][c-1]+=1
		for i in range(n):#printing 2-D array after increasing by with their respective positions
			print(a[i])
		print(oddcount(a,n,m))