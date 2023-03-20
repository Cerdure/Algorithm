def solution(b, s):
    def f(n):
        i=1
        while n:i*=n;n-=1
        return i
    return f(b)/(f(b-s)*f(s))