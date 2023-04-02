def solution(s):
    r=[0]*2
    while s!='1':
        r[0]+=1
        r[1]+=s.count('0')
        s=str(bin(len(s)-s.count('0'))[2:])
    return r