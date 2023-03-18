size,_,*num=map(int,open(0).read().split())
list=[0]*size
while num:
  i,j,k,*num=num
  list[i-1:j]=[k]*(j-i+1)
print(*list)