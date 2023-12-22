#現在要試著模擬看看
s='00111'
N=len(s)#長度
zero=0 #等一下也要
one=0 #想找出全部的一
for i in range(N):
  if s[i]=='1': one +=1
#現在就知道總共有幾個one
print('一開始的時候,都在右邊,統計結果','zero',zero,'one',one)
ans=0
for i in range(N-1):
  if s[i]=='0':
    zero += 1
  if s[i]=='1':
    one -= 1
  print('中間過程中,','zero',zero,'one',one)
  ans=max(ans,zero+one)
print('答案找出來了',ans)