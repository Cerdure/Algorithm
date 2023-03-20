def solution(s):
    s=s.split(' ')
    x=int(s[0])
    for i,n in enumerate(s):
        if not n.isdigit():
            x+=int(s[i+1])*(2*(n=='+')-1)
    return x