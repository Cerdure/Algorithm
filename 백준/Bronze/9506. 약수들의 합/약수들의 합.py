while (n:=int(input()))!=-1:
  l=[i for i in range(1,n//2+1) if n%i==0]
  if sum(l)==n:print(str(n)+' = '+' + '.join(map(str,l)))
  else:print(str(n)+' is NOT perfect.')