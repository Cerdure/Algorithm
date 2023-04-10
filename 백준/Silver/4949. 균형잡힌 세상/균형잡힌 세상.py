for s in open(0).read().split('.')[:-2]:
  l=[]
  for c in s:
    if c in ('(','['):l.append(c)
    try:
      if c==')':
        if l.pop()!='(':l+=[0];break
      if c==']':    
        if l.pop()!='[':l+=[0];break
    except:l+=[0];break
  print(['yes','no'][len(l)>0])