d=[[+(i==1)]*10 for i in range(101)];d[1][0]=0
for i in range(2,(n:=int(input()))+1):
    for j in range(10):
      if j==0:d[i][j]=d[i-1][1]
      elif j==9:d[i][j]=d[i-1][8]
      else:d[i][j]=d[i-1][j-1]+d[i-1][j+1]
print(sum(d[n])%1000000000)