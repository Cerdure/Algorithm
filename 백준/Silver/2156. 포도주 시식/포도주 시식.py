n,*l=map(int,open(0))
d=[l[0]]+[0]*(n-1)
if n>1:d[1]=l[0]+l[1]
if n>2:d[2]=max(d[1],l[2]+l[0],l[2]+l[1])
for i in range(3,n):d[i]=max(d[i-1],l[i]+l[i-1]+d[i-3],l[i]+d[i-2])
print(d[n-1])