n,*l=open(0);d=[0]*501
for _,i in sorted([*map(int,i.split())] for i in l):d[i]=max(d[:i])+1
print(int(n)-max(d))