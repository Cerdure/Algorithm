n,m,*l=map(int,open(0).read().split())
q,c=list(range(1,n+1)),0
for i in l:
  if q.index(i)<len(q)//2+1:
    while q[0]!=i:q=q[1:]+q[:1];c+=1
    q=q[1:]  
  else:
    while q[0]!=i:q=q[-1:]+q[:-1];c+=1
    q=q[1:]
print(c)