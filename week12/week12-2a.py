#a=[1 1 2 3 5 8 13 21]
a=[1,1]
for i in range(2,100):
  a.append(a[i-1]+a[i-2])
  #a[i]=a[i-1]+a[i-2]
print(a)