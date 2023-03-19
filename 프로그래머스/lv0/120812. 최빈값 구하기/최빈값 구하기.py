def solution(array):
    l=[array.count(i) for i in range(0,max(array)+1)]
    m=l.index(max(l))
    return m if l.count(l[m])==1 else -1