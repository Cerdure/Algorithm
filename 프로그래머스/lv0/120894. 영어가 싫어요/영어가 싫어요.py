def solution(n):
    m=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in range(10):n=n.replace(m[i],str(i))
    return int(n)