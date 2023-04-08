import sys
input=sys.stdin.readline
s=set()
for _ in range(int(input())):
  k,v=input().split()
  if v=='leave':s.remove(k)
  else:s.add(k)
for i in sorted(s,reverse=True):print(i)