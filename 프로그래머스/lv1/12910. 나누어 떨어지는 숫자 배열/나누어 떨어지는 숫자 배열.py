def solution(a, d):
    l=sorted([i for i in a if i%d==0])
    l= [-1] if len(l)<1 else l
    return l