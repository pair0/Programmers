from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((numbers[0], 0))
    queue.append((-1 * numbers[0], 0))

    while queue:
        temp, index = queue.popleft()
        index += 1
        if index < len(numbers):
            queue.append((temp + numbers[index], index))
            queue.append((temp - numbers[index], index))
        else:
            if temp == target:
                answer += 1
    return answer
