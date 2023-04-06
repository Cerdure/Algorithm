l=[[0]*100 for _ in range(100)]
for _ in range(int(input())):
  x1,y1=map(int,input().split())
  for x2 in range(10):
    for y2 in range(10):
      l[x1+x2][y1+y2]=1
print(sum(map(sum,l)))