def solution(n):
    answer = 0
    add = 0

    if n % 7 != 0:  # 7로 나누어 떨어지지 않는 경우 +1을 해준다.
        add = 1

    answer = (n // 7) + add

    return answer
