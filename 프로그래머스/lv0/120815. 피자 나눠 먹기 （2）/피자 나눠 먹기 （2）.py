def solution(n):
    a,b=n,6
    while(b):a,b=b,a%b
    return n/a