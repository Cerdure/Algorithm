import sys
r=sys.stdin.readline
p=[1]*1000001
for i in range(2,1001):
  for j in range(i*2,1000001,i):
    if p[j]:p[j]=0
for _ in range(int(r())):
  n,c=int(r()),0
  for i in range(2,n//2+1):
    if p[i] and p[n-i]:c+=1
  print(c)