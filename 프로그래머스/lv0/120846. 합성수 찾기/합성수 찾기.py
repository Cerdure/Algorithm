def solution(n):
    def divisor(i):
        for x in range(2,int(i**0.5)+1): 
            if i%x==0: return True
        return False
    return len([i for i in range(4,n+1) if divisor(i)])