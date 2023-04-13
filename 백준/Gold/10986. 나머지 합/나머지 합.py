n,m,*a=map(int,open(0).read().split())
p,t,c=[1]+[0]*(m-1),0,0
for i in range(n):p[(t:=t+a[i])%m]+=1
for i in p:c+=i*(i-1)//2
print(c)