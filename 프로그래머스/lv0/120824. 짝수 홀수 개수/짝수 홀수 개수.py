def solution(num_list):
    def cnt(type):return len([i for i in num_list if i%2==type])
    return [cnt(0),cnt(1)]