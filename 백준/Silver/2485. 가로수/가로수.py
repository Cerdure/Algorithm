import sys
input=sys.stdin.readline
l=[int(input()) for _ in range(int(input()))]
g=l[1]-l[0]
for i,v in enumerate(l[1:]):
  p=l[i]=v-l[i]
  while p:g,p=p,g%p
print(sum(i//g-1 for i in l[:-1]))