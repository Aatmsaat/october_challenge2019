t=int(input())
for _ in range(t):
	n,m,q=list(map(int,input().split()))
	count=0
	cc={}#count for number of columns unchecked
	cr={}#count for number of rows unchecked
	while q:
		q-=1
		count=0
		r,c=list(map(int,input().split()))
		if c in cc:
			cc.pop(c)
		else:
			cc[c]=0
		if r in cr:
			cr.pop(r)
		else:
			cr[r]=0
	cc=len(cc)#counting number of left columns
	cr=len(cr)#counting number of left rows
	if cc == cr:
		if m == n and cc ==m:
			count=0
		else:
			r1=0#ranges from 0
			r2=cc-1#to cc-1
			count=cc*(m+n-2) - 4*(r2-r1+1)*(r1+r2)//2
	elif cc > cr:
		# cr is counting unmatched positions
		cc-=cr
		r1=(cc+1)//2
		r2=r1+cr-1
		count=n*cc + cr*(m+n-2) - 4*(r2-r1+1)*(r1+r2)//2
	elif cr > cc:
		# cc is counting unmatched positions
		cr-=cc
		r1=(cr+1)//2
		r2=r1+cc-1
		count=m*cr + cc*(m+n-2) - 4*(r2-r1+1)*(r1+r2)//2
	print(count)