def solution(d):
    d=sorted(d,key=lambda x:x[0]+x[1])
    c1=abs(d[0][0]-d[1][0])/abs(d[0][1]-d[1][1])==abs(d[2][0]-d[3][0])/abs(d[2][1]-d[3][1])
    c2=abs(d[0][0]-d[2][0])/abs(d[0][1]-d[2][1])==abs(d[1][0]-d[3][0])/abs(d[1][1]-d[3][1])
    return (c1 | c2)*1