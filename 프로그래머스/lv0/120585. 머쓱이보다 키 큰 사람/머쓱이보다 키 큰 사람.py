def solution(array, height):
    return len(list(filter(lambda _:_>height,array)))
