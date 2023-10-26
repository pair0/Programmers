import heapq

def solution(ability, number):
    answer = 0
    heap = []
    for i in ability:
        heapq.heappush(heap, i)
        
    for i in range(number):
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        a, b = a+b, a+b
        heapq.heappush(heap, a)
        heapq.heappush(heap, b)
                       
    answer = sum(heap)
    return answer