from heapq import heappush, heappop


def solution(operations):
    answer = []
    heap = []  # 최대 힙

    for i in operations:
        list1 = i.split(" ")
        if list1[0] == "I":  # 큐에 주어진 숫자 삽입
            heappush(heap, int(list1[1]))
        else:
            if len(heap) > 0:
                if int(list1[1]) == 1:  # 최댓값 삭제
                    heap.remove(max(heap))
                else:  # 최솟값 삭제
                    heappop(heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), min(heap)]

    return answer
