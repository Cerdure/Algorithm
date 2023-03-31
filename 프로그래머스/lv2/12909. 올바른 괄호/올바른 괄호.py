def solution(s):
    c,s=0,s.replace('(',' 1').replace(')',' -1')[1:].split(' ')
    for i in s:
        c+=int(i)
        if c==-1:return False
    return c==0