import math


def solution(progresses, speeds):
    answer = []
    count = 1
    remainder = math.ceil((100 - progresses[0]) / speeds[0])

    for i in range(1, len(progresses)):
        next_remainder = math.ceil((100 - progresses[i]) / speeds[i])
        if remainder >= next_remainder:
            count += 1
        else:
            remainder = next_remainder
            answer.append(count)
            count = 1

    answer.append(count)

    return answer
