n,*l=open(0)
l=sorted([list(map(int,i.split())) for i in l],key=lambda x:x[0])
d=[1]*(n:=int(n))
for i in range(n):
  for j in range(i):
    if l[i][1]>l[j][1] and d[i]<=d[j]:d[i]=d[j]+1 
print(n-max(d))