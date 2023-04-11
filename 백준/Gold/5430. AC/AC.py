from collections import deque
a=[*open(0)][1:]
pl,l=a[::3],a[2::3]
for p,i in zip(pl,l):
  try:
    i=deque(i[1:-2].split(','))
    p,d=p[:-1],0
    for s in p:
      if s=='R':d=~d
      else:
        if i[0]=='':raise
        if -d:i.pop()
        else:i.popleft()
    if -d:i.reverse()      
    print('['+','.join(i)+']')
  except:print('error')