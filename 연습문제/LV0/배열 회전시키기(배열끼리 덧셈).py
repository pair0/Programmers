def solution(numbers, direction):
    answer = []

    if direction == "right":
        for i in range(len(numbers)):
            answer.append(numbers[i - 1])
    elif direction == "left":
        for i in range(len(numbers)):
            if i+1 >= len(numbers):
                i = (i+1) % len(numbers) - 1
            answer.append(numbers[i + 1])

    return answer


# 다른 풀이
def solution(numbers, direction):
    n = len(numbers)
    if direction == 'left':
        return numbers[1:n] + [numbers[0]]
    else:
        return [numbers[n-1]] + numbers[0:n-1]
