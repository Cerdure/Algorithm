l=[input().split() for _ in range(int(input()))]
l=[int(y) for x in l for y in x]
x,y=map(sorted,[l[::2],l[1::2]])
print((x[-1]-x[0])*(y[-1]-y[0]))