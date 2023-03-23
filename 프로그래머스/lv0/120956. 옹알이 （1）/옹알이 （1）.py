def solution(bb):
    for i,b in enumerate(bb):
        ayaya,s=["aya", "ye", "woo", "ma"],0
        for x in range(0,len(b)):
            if b[0:x-s+1] in ayaya:
                ayaya.remove(b[0:x-s+1])
                b,s=b[x-s+1:],x+1
        bb[i]=b
    return bb.count('')