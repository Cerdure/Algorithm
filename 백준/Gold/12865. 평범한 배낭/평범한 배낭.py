l=[*map(lambda x:[*map(int,x.split())],open(0))]
n,k=l[0]
l[0]=[0,0]
s=[[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        w,v=l[i]
        if j<w:s[i][j]=s[i-1][j]
        else:s[i][j]=max(v+s[i-1][j-w],s[i-1][j])
print(s[n][k])