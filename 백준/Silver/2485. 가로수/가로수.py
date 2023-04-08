n,x=map(int,(input(),input()))
l=[]
for _ in range(n-1):
  l.append((i:=int(input()))-x)
  x=i
x=l[0]  
for i in l[1:]:
  while i:x,i=i,x%i
print(sum([i//x-1 for i in l]))