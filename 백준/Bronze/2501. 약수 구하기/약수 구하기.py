n,k=map(int,input().split())
l=[i for i in range(1,n//2+1) if n%i==0]+[n]
try:print(l[k-1])
except:print(0)