def solution(k, b):
    x=[0,0]
    def move(i,n,s1,s2):
        x[n]=x[n]-(i==s1 and x[n]-1>-b[n]//2)+(i==s2 and x[n]<b[n]//2)
    for i in k:
        move(i,0,'left','right')
        move(i,1,'down','up')
    return x
    