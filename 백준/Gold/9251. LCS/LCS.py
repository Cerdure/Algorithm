a,b=open(0).read().split()
l1,l2,r=len(a),len(b),range
d=[[0]*(l2+1) for _ in r(l1+1)]
for i in r(1,l1+1):
  for j in r(1,l2+1):
    if a[i-1]==b[j-1]:d[i][j]=d[i-1][j-1]+1
    else:d[i][j]=max(d[i-1][j],d[i][j-1])
print(d[-1][-1])