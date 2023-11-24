from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque()
    time = deque()

    queue.append(truck_weights.pop(0))
    answer += 1
    time.append(answer + bridge_length)

    while len(truck_weights) != 0:
        if sum(queue) + truck_weights[0] <= weight:
            queue.append(truck_weights.pop(0))
            answer += 1
            time.append(answer + bridge_length)
            if answer == time[0]:
                queue.popleft()
                time.popleft()
        else:
            answer = time.popleft()
            queue.popleft()
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
                time.append(answer + bridge_length)

    answer = time.pop()
    return answer
