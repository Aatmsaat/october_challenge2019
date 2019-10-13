#first making sieve to find prime factorization
import math
mxn=1000001
spf=[0]*mxn #list of smallest prime factors
spf[1]=1 #Since 1 is composite not prime
# Now making 2 divisible no.s
for i in range(2,mxn):
	spf[i] = i

for i in range(4,mxn,2):# 2 divisible no.s replaced by 2
	spf[i]=2

mxnsqrt=math.ceil(math.sqrt(mxn))
for i in range(3,mxnsqrt):# No. divisible by 3 and other prime no.s replaced by 3 and others respectively
	if(spf[i] == i):
		for j in range(i*i,mxn,i):
			if (spf[j]==j): # checking if already not marked
				spf[j]=i				

t=int(input())
while t:
	t-=1
	n=int(input())
	positioncount=[0]*mxn # to count positions of prime factors
	a=list(map(int,input().split()))
	star=0
	for i in range(n):
		val=a[i]
		if val == 1:
			star=i
		elif positioncount[val] > star:
			star=positioncount[val]
		#Now counting no. of prime factors
		flagfac=[True]*mxn# for counting prime factors only once
		while(val!=1):
			x=spf[val]
			if flagfac[x]:
				positioncount[x]+=1
				flagfac[x]=False
			if flagfac[val]:
				positioncount[val]+=1
				flagfac[val]=False
			val=val//x
	print(star)