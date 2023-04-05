n=int(input())
for i in range(1,n*2):
  print(' '*abs(n-i)+'*'*(n*2-abs(n-i)*2-1))