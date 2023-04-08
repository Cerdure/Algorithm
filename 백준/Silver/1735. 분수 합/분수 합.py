a1,b1,a2,b2=map(int,open(0).read().split())
x,y=s,m=a1*b2+a2*b1,b1*b2
while y:x,y=y,x%y
print(s//x,m//x)