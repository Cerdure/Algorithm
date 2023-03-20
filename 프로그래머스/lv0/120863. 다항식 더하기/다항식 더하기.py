def solution(p):
    p=p.split(' ')
    x=str(sum([1 if i=='x' else int(i[:-1]) for i in p if 'x' in i]))
    n=str(sum([int(i) for i in p if i.isdigit()]))
    x='' if x=='1' else x
    x=x+'x + '+n if x!='0' else n
    return x.replace(' + 0','')