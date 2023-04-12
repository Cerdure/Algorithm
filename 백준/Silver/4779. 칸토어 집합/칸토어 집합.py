def c(s,e,l):
  if s==e:l[s]='-'
  else:
    d=(e-s+1)//3-1
    c(s,s+d,l);c(e-d,e,l)
for i in open(0):
  n=3**int(i)
  c(0,n-1,l:=[' ']*n)
  print(''.join(l))