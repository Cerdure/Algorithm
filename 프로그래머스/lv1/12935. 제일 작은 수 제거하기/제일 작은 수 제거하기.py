def solution(a):
    a.remove(min(a))
    a=[-1] if len(a)<1 else a
    return a