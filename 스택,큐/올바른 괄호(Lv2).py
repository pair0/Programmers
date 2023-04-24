from collections import deque


def solution(s):
    answer = True
    queue = deque()

    for i in s:
        if i == "(":
            queue.append(')')
        else:
            if not queue:
                return False
            queue.popleft()

    if queue:
        answer = False
    else:
        answer = True
    return answer
