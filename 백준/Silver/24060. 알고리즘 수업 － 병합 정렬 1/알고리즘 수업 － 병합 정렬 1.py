def s(l,p,r):
    if p<r and c<=k:
        s(l,p,q:=(p+r)//2)
        s(l,q+1,r)
        m(l,p,q,r)
def m(l,p,q,r):
    global c,x;i,j,a=p,q+1,[]
    while i<=q and j<=r:
        if(l[i]<=l[j]):a.append(l[i]);i+=1
        else:a.append(l[j]);j+=1
    while i<=q:a.append(l[i]);i+=1
    while j<=r:a.append(l[j]);j+=1
    i,t=p,0
    while i<=r:
        l[i]=a[t];c+=1
        if c==k:x=l[i];break
        i+=1;t+=1
n,k,*l=map(int,open(0).read().split())
c,x=0,-1
s(l,0,n-1)
print(x)