s,_,*l=open(0)
for i in l:
  c,f,e=i.split()
  print(s[int(f):int(e)+1].count(c))