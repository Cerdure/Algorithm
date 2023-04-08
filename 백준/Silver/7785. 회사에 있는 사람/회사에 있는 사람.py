import sys
d=dict([(sys.stdin.readline().split()) for _ in range(int(sys.stdin.readline()))])
s=sorted(set(k for k,v in d.items() if v=='enter'),reverse=True)
for i in s:print(i)