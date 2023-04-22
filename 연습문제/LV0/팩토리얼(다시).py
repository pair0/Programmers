def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def solution(n):
    answer = 0

    while 1:
        answer += 1
        if factorial(answer) == n:
            break
        elif factorial(answer) > n:
            answer -= 1
            break
    return answer
