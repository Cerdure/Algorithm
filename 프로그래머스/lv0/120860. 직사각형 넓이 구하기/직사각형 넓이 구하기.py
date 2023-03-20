def solution(d):
    x,y=sorted([i[0] for i in d]),sorted([i[1] for i in d])
    return (x[0]-x[-1])*(y[0]-y[-1])
