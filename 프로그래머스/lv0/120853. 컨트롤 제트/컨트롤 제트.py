def solution(s):
    x=0
    for i,n in enumerate(s:=s.split(' ')):
        x-=int(s[i-1]) if n=='Z' else -int(n)
    return x