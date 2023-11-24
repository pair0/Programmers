from heapq import heappush, heappop, heapify


def solution(stones, k):
    heap = [(-1 * val, idx) for idx, val in enumerate(stones[:k])]
    heapify(heap)
    answer = -1 * heap[0][0]

    for i in range(k, len(stones)):
        heappush(heap, (-1 * stones[i], i))
        while heap[0][1] <= i - k:
            heappop(heap)
        answer = min(answer, -1 * heap[0][0])

    return answer
