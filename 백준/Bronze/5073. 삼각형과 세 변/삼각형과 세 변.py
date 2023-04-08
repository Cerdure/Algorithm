while (l:=sorted(map(int,input().split())))[2]!=0:
  print('Invalid' if l[0]+l[1]<=l[2] 
        else 'Equilateral' if l[0]==l[2] 
        else 'Scalene' if l[0]!=l[1]!=l[2] 
        else 'Isosceles')