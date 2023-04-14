def solution(sizes):
    answer = 0
    max_x, max_y = 0, 0

    for i, j in sizes:
        if i < j:
            i, j = j, i
        if max_x < i:
            max_x = i
        if max_y < j:
            max_y = j

    answer = max_x * max_y

    return answer
