def solution(num):
    c=0
    while c<500: 
        if num==1:return c
        if num%2==0:num//=2
        else:num=num*3+1
        c+=1
    return -1    
