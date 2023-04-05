s=['F','','D0','D+','C0','C+','B0','B+','A0','A+']
l=[input().split(' ') for _ in range(20)]
gs,ls=0,0
for i in l:
  if i[2]=='P':continue
  g=float(i[1][0])
  gs+=g
  ls+=g*s.index(i[2])/2
print(ls/gs)