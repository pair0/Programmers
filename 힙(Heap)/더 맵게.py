# 모든 음식의 스코빌 지수 K 이상
# 섞은 음식 = 가장 맵지 않은 + (두 번째로 맵지 않은 *2)
from heapq import heappush, heappop, heapify


def solution(scoville, K):
    answer = 0
    heapify(scoville)
    minV = heappop(scoville)

    while minV < K:
        if len(scoville) < 1:
            return -1
        minS = heappop(scoville)
        mix = minV + (minS * 2)
        heappush(scoville, mix)
        answer += 1
        minV = heappop(scoville)

    return answer
