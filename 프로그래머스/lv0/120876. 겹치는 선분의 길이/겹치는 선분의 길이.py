def solution(l):
    s=sorted(sum(l,[]))
    min,max=s[0],s[-1]
    d=dict.fromkeys(range(min,max+1),0)
    for i in l:
        for j in range(i[0]+1,i[1]+1):d[j]+=1
    return len(list(filter(lambda x:x[1]>1,d.items())))  
    