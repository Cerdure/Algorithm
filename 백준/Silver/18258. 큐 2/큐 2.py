c,l=0,[]
for i in open(0):
  try:
    if (i:=i[:-1]).isdigit():continue
    if 'push' in i:l.append(i.split()[1])
    if i=='pop':print(l[c]);c+=1
    if i=='size':print(len(l)-c)
    if i=='empty':print(+(len(l)==c))
    if i=='front':print(l[c])
    if i=='back':print(l[-1] if len(l)>c else -1)
  except:print(-1)