n,m=map(int,input().split())
l=list(range(1,n+1))
for i in range(m):
  a,b=map(lambda x:int(x)-1,input().split())
  l[a:b+1]=reversed(l[a:b+1])
print(*l)