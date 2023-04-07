n,p=int(input()),4
for i in range(n):p+=sum([j for j in range(4,2**i*4+1,4)])+4**i
print(p)