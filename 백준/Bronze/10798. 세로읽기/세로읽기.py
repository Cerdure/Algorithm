l,s=[list(input()) for _ in range(5)],''
for _ in range(max(map(len,l))):
  for i in l:
    if len(i)==0:continue
    s+=i.pop(0)
print(s)  