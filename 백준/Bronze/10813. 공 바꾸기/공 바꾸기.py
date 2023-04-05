n,m=map(int,input().split())
l=list(range(1,n+1))
for i in range(m):
  a,b=map(lambda x:int(x)-1,input().split())
  l[a],l[b]=l[b],l[a]
print(' '.join(map(str,l)))