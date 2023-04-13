_,a,*l=open(0)
p,l=[0],[[*map(int,i.split())] for i in l]
for i,v in enumerate(a.split()):p.append(p[i]+int(v))
for i in l:print(p[i[1]]-p[i[0]-1])