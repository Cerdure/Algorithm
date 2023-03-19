def solution(numbers, direction):
    d=1-(direction=="right")*2
    return numbers[d:]+numbers[:d]