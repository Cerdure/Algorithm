def solution(s):
    s=[(i[0]+i[1])/2 for i in s]
    d={n:len(s)-i for i,n in enumerate(sorted(s))}
    return [d[i] for i in s]