def solution(c):
    s=0
    while c>9:s+=c//10;c=c//10+c%10
    return s
  