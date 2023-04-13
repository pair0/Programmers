def solution(players, callings):
    hash_map = {p: i for i, p in enumerate(players)}

    for i in callings:
        tmp = hash_map[i] - 1
        hash_map[players[tmp]], hash_map[i] = hash_map[i], tmp
        players[tmp], players[tmp+1] = players[tmp+1], players[tmp]

    return players
