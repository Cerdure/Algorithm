def solution(n):
    a=1
    for i in range(1,n):
        if n%i==0: a+=1
    return a