def solution(array, n):
    array.append(n)
    array.sort()
    i=array.index(n)
    try: a=array[i-1] 
    except: return array[i+1]
    try: b=array[i+1] 
    except: return array[i-1]
    return a if n-a<=b-n else b