def solution(n):
    c=1
    for i in range(1,n//2+1):
        s=0
        for j in range(i,n//2+2):
            s+=j
            if s==n:c+=1
            elif s>n:break 
    return c