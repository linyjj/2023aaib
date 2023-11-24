a,b=list(map(int,input().split()))
if a>b:#be careful! who is small
	a,b=b,a #change a and b
for i in range(a,b+1):
	if i%5==0: print(i)