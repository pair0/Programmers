def solution(n):
    answer = 0

    if (n ** (1/2)) % 1 == 0:  # (루트 : n ** (1/2)), ### (자연수인지 소수인지 판별 : 1로 나누었을 때 나머지가 있으면 소수)
        answer = 1
    else:
        answer = 2
    return answer
