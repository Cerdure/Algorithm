def solution(a,b):
    c=b
    while c:a,c=c,a%c
    b//=a
    s=[i for i in range(2,b+1) if b%i==0 and i%2!=0 and i%5!=0]
    return -~(len(s)>0)