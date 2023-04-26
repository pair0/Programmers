def solution(array):
    hash_map = dict()

    for index, value in enumerate(array):
        hash_map[value] = index

    hash_map = sorted(hash_map.items(), reverse=True)
    return list(hash_map[0])
