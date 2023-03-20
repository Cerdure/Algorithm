solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]
# sort의 기준으로 key 사용
# key를 함수로 제공(len, lambda 등), (abs(x-n),x) -> (key1,key2)
