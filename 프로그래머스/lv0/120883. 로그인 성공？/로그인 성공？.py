def solution(i,d):
    try:return 'login' if dict(d)[i[0]]==i[1] else 'wrong pw'
    except:return 'fail'