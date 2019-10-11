t=int(input())
for _ in range(t):
	n,m,q=list(map(int,input().split()))
	#Making 2-D array with the given dimensions n->rows 
	#and m-> columns initializing them zero
	a=[0]*n
	for i in range(n):
		a[i]=[0]*m
	count=0
	while q:
		q-=1
		count=0
		r,c=list(map(int,input().split()))
		for i in range(m):
			a[r-1][i]+=1
		for i in range(n):
			a[i][c-1]+=1
		print()
		for i in range(n):
			for j in range(m):
				if a[i][j]%2!=0:
					count+=1
					print('1',end=' ')
				else:
					print('0',end=' ')
			print()
		print(f'{count} \n')
	#print(count)