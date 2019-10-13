def remainingsame1(a,n,k):
	half=n//2
	ans=[]
	if k < half:
		for i in range(k,half):
			ans.append(a[i]^a[n-1-i])
		if n%2!=0:
			ans=ans+[0]
		ans=ans+a[half-1::-1]
	else:
		if n%2!=0 and k==half:
			ans=[0]
			k+=1
		ans=ans+a[n-k-1::-1]
	return ans

def remainingsame2(a,n,k):
	half=n//2
	ans=[]
	if k < half:
		r1=n-1-half
		ans=a[n-1-k:r1:-1]
		if n%2!=0:
			ans=ans+[0]
		i=half-1
		while i >= 0:
			ans.append(a[i]^a[n-1-i])
			i-=1
	else:
		if n%2!=0 and k==half:
			ans=[0]
			k+=1
		i=n-1-k
		while i>=0:
			ans.append(a[i]^a[n-1-i])
			i-=1
	return ans
	
t=int(input())
while t:
	t-=1
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	k-=1
	half=n//2
	if k>n and n%2!=0:
		a[half]=0
	ans=[]
	k=k%(3*n)
	if k<n:
		#half=n//2
		if n==1:
			ans=[0]
		elif k < half:
			for i in range(k+1):
				ans.append(a[i]^a[n-1-i])
			ans=ans+a[k+1::]
		else:
			for i in range(half):
				ans.append(a[i]^a[n-1-i])
			r1=2*half-k-1#half-1-(k-half-1)
			if n%2!=0:
				ans=ans+[0]
				r1+=1
			if k==n-1:
				ans=ans+a[half-1::-1]
			else:
				ans=ans+a[half-1:r1-1:-1]+a[k+1::]
	elif k<2*n:
		#half=n//2
		k%=n
		if k < half:
			r1=n-k-2
			ans=a[n-1:r1:-1]+remainingsame1(a,n,k+1)#a[k+1::]
		else:
			r1=n-1-half
			ans=a[n-1:r1:-1]
			r1=2*half-k-1#half-1-(k-half-1)
			if n%2!=0:
				ans=ans+[0]
				r1+=1
			if k==n-1:
				#ans=ans+a[half-1::-1]
				i=half-1
				while i>=0:
					ans.append(a[i]^a[n-1-i])
					i-=1	
			else:
				#ans=ans+a[half-1:r1-1:-1]+a[k+1::]
				for i in range(half-1,r1-1,-1):
					ans.append(a[i]^a[n-1-i])
				ans=ans+remainingsame1(a,n,k+1)#a[k+1::]
	else:
		ans=a
		#half=n//2
		k%=(2*n)
		if n%2!=0:
			ans[half]=0
		ans=ans[:k+1:]+remainingsame2(a,n,k+1)
	for i in ans:
		print(i,end=" ")
	print()