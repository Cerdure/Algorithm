for i in range((n:=int(input()))-1,0,-1):n*=i
print(n if n>0 else 1)