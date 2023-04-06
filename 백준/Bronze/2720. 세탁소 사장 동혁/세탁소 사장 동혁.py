for i in [int(input()) for _ in range(int(input()))]:
  a,i=divmod(i,25)
  b,i=divmod(i,10)
  c,i=divmod(i,5)
  d,i=divmod(i,1)
  print(a,b,c,d)