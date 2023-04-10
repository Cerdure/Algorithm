l=[*open(0)][1:]
for m,d in zip(l[::2],l[1::2]):
  m,c=int(m.split()[1]),1
  d=list(map(int,d.split()))
  q=list(range(r:=len(d)))
  while r>0:
    if d[0]==max(d):
      if q[0]==m:print(c);break
      d,q=d[1:],q[1:];c+=1
    else:d,q=d[1:]+d[:1],q[1:]+q[:1]