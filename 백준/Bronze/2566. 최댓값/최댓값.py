c=[map(int,input().split(' ')) for _ in range(9)]
m=[-1,0,0]
for i1,v1 in enumerate(c):
  for i2,v2 in enumerate(v1):
    if v2>m[0]:m=v2,i1+1,i2+1
print(m[0])
print(*m[1:])