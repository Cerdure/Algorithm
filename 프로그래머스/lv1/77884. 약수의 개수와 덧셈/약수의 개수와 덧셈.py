solution=lambda l,r:sum([i*d(i) for i in range(l,r+1)])
def d(n):
    return (len([i for i in range(1,n//2+1) if i!=n and n%i==0])%2!=0)*2-1