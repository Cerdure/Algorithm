def solution(numer1, denom1, numer2, denom2):
    numer=numer1*denom2+numer2*denom1
    denom=denom1*denom2
    y,x=[numer,denom]
    while(y):x,y=y,x%y
    return [numer/x,denom/x]