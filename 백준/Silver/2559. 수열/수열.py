n,k,*l=map(int,open(0).read().split())
d=[sum(l[:k])]
for i in range(n-k):d.append(d[i]-l[i]+l[i+k])
print(max(d))