def c(s,f,e):
  if f>=e:return'1 '+str(f+1)
  elif s[f]!=s[e]:return'0 '+str(f+1)
  else:return c(s,f+1,e-1)
for s in [*open(0)][1:]:print(c(s:=s[:-1],0,len(s)-1))