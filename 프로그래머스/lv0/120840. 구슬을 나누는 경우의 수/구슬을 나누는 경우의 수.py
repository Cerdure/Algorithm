solution=lambda b,s:f(b)/(f(b-s)*f(s))    
def f(n):
    i=1
    while n:i*=n;n-=1
    return i
