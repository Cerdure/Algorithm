l,n,r=[],0,''
for i in [*open(0)][1:]:
  i=int(i)
  while n<i:n+=1;l.append(n);r+='+\n'
  if l.pop()!=i:r='NO';break
  else:r+='-\n'  
print(r)