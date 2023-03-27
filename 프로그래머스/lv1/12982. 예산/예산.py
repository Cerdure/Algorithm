def solution(d, b):
    s=0
    for i,v in enumerate(sorted(d)):
        s+=v
        if s>b:return i
    return len(d)