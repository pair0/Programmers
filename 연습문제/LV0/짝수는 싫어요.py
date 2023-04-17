# 풀이 1
def solution(n):
    answer = [i for i in range(1, n+1) if i % 2 != 0]
    return answer


# 풀이 2
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 != 0:
            answer.append(i)
    return answer
