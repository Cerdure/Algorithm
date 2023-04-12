n,*l=map(int,open(0).read().split())
ld,rd=[1]*n,[1]*n
for i in range(n):
  for j in range(i):
    if(l[i]>l[j] and ld[i]<=ld[j]):ld[i]=ld[j]+1
    if(l[~i]>l[~j] and rd[~i]<=rd[~j]):rd[~i]=rd[~j]+1
print(max(map(sum,zip(ld,rd)))-1)