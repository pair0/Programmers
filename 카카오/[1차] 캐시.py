# LRU
# cache hit => 1
# cache miss => 5
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    # cache = [] * cacheSize
    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for i in cities:
        i = i.lower()
        if i not in cache:  # cache miss
            answer += 5
            if len(cache) < cacheSize:
                cache.append(i)
            else:
                cache.popleft()
                cache.append(i)
        else:  # cache hit
            answer += 1
            cache.remove(i)
            cache.append(i)

    return answer
