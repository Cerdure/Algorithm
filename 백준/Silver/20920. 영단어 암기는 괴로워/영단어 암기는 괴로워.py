import sys
r=sys.stdin.readline
n,m=map(int,r().split())
l={}
for _ in range(n):
  if len(s:=r()[:-1])>=m:
    try:l[s]+=1
    except:l[s]=1
for i in sorted(l,key=lambda x:(-l[x],-len(x),x)):
  print(i) 