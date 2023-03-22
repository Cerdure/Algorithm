def solution(b):
    n=len(b)
    for i1,v1 in enumerate(b):
        for i2,v2 in enumerate(v1):
            if v2==1:
                pi1=0 if i1<1 else i1-1
                pi2=0 if i2<1 else i2-1
                ni1=n if i1>n-2 else i1+2
                ni2=n if i2>n-2 else i2+2
                for x in range(pi1,ni1):
                    for y in range(pi2,ni2):
                        b[x][y]=9 if b[x][y]!=1 else 1
    return sum(b,[]).count(0)

    
    
            
              
   
