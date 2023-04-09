import sys
r=sys.stdin.readline
def pn(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:return 0
  return 1 if n>1 else 0
for _ in range(int(r())):
  n=int(r())
  while 1:
    if pn(n):break
    n+=1
  print(n)