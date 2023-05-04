def solution(score):
    hash_map = dict()
    same = -1
    count = 0
    flag = 0

    for i, (j, k) in enumerate(score):
        hash_map[i+1] = (j+k)/2

    hash_map = dict(sorted(hash_map.items(), reverse=True, key=lambda x: x[1]))

    for i, j in hash_map.items():
        if same == j:
            hash_map[i] = count
            flag += 1
            same = j
        else:
            count += (1+flag)
            flag = 0
            same = j
            hash_map[i] = count

    hash_map = dict(sorted(hash_map.items()))
    answer = [*hash_map.values()]
    return answer


# 다른 풀이
def solution(score):
    answer = []
    li = []

    for i in score:
        li.append(sum(i)/len(i))
    sort_arr = sorted(li, reverse=True)

    for i in li:
        answer.append(sort_arr.index(i)+1)

    return answer
