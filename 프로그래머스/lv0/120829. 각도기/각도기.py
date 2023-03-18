def solution(angle):
    answer = int("1234"[angle%90==0::2][angle>90])
    return answer