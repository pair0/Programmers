def solution(numbers):
    answer = 0
    N = len(numbers)
    for i in numbers:
        answer += i

    answer = answer / N
    return answer
