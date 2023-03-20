def solution(n):
    i=0
    while n:
        i+=1
        if '3' not in str(i) and i%3!=0:n-=1
    return i