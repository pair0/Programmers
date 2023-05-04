def solution(numlist, n):
    numlist.sort(reverse=True)
    hash_map = dict()

    for i in numlist:
        hash_map[i] = abs(i - n)

    hash_map = dict(sorted(hash_map.items(), key=lambda x: x[1]))
    answer = [*hash_map.keys()]

    return answer
