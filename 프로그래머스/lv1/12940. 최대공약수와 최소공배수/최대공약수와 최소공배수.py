def solution(n, m):
    g,s,x=0,0,n*m
    while m:n,m=m,n%m
    return [n,x//n]