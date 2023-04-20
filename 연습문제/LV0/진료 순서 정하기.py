def solution(emergency):
    answer = []

    hash_map = {p: i+1 for i, p in enumerate(sorted(emergency, reverse=True))}

    for i in emergency:
        answer.append(hash_map[i])

    return answer
