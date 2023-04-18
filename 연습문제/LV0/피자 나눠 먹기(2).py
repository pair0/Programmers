def solution(n):
    answer = 0

    # 피자의 1판의 갯수인 6과 피자를 먹는 사람 n의 최소 공배수를 구한다.
    for i in range(max(n, 6), n*6+1):
        if i % n == 0 and i % 6 == 0:
            answer = i // 6
            break

    return answer
