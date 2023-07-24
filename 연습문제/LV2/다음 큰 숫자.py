def solution(n):
    answer = 0

    c = bin(n).count("1")
    for m in range(n + 1, 1000001):
        if bin(m).count("1") == c:
            answer = m
            break

    return answer

