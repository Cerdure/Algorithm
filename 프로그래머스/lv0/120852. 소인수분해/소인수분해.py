def solution(n):
    l=[i for i in range(2,int(n**1/2)+1) if n%i==0]
    l.append(n)
    for n in l:l=[x for x in l if x==n or x%n!=0]
    return l
