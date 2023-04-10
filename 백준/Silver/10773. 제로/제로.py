q=[]
for i in [*open(0)][1:]:
  if i=='0\n':q.pop()
  else:q.append(int(i[:-1]))
print(sum(q))