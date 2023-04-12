n,*l=map(int,open(0).read().split())
d,r=[1]*n,range
for i in r(n):
  for j in r(i):
    if l[i]>l[j] and d[i]<=d[j]:d[i]=d[j]+1
print(max(d))