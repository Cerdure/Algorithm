l=open(0).read().split('\n')[1:]
r={'ChongChong'}
for s in l:
  s={*s.split()}
  if len(s-r)==1:r=r|s    
print(len(r))