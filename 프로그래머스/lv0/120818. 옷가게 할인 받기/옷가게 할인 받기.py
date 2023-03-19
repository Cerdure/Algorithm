def solution(price):
    return int(price*(0.8 if price>=5e5 else 0.9 if price>=3e5 else 0.95 if price>=1e5 else 1))