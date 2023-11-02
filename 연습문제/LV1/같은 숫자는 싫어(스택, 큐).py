from collections import deque


def solution(arr):
    answer = []
    lens = len(arr)
    queue = deque([arr[0]])
    x = arr[0]

    for i in range(1, lens):
        if x != arr[i]:
            x = arr[i]
            answer.append(queue.popleft())
            queue.append(arr[i])

    x = queue.popleft()
    answer.append(x)

    return answer
