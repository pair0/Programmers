# 한 번에 하나의 작업만 수행
from heapq import heappush, heappop


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    N = len(jobs)

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1]
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))

    return answer
