def solution(numbers, k):
    answer = 0

    num = (2 * k - 1) % len(numbers)

    answer = numbers[num-1]

    return answer
