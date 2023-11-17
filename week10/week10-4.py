a=int(input())
ans=100

if a>2000:
	ans+=(a-2000)//500*5
	if(a-2000)%500:ans+=5
	
print(ans)