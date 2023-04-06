n,b=map(int,input().split())
r=''
while n>0:
  n,m=divmod(n,b)
  if m>9:m=chr(m+55)
  r+=str(m)
print(r[::-1])