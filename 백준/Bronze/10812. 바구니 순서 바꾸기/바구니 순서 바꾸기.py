n,m=map(int,input().split())
l=list(range(1,n+1))
for _ in range(m):
  a,b,c=map(int,input().split())
  l=l[:a-1]+l[c-1:b]+l[a-1:c-1]+l[b:]
print(*l)