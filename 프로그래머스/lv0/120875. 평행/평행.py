def solution(d):
    d=sorted(d,key=lambda x:x[0]+x[1])
    x1,y1,x2,y2,x3,y3,x4,y4=sum(d,[])
    c1=abs((x1-x2)/(y1-y2))==abs((x3-x4)/(y3-y4))
    c2=abs((x1-x3)/(y1-y3))==abs((x2-x4)/(y2-y4))
    return (c1 | c2)*1
