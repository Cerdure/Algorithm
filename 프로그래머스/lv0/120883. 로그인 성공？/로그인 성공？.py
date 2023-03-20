def solution(i,d):
    d=dict(d)
    try:return 'login' if d[i[0]]==i[1] else 'wrong pw'
    except:return 'fail'