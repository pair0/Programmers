def solution(num_list, n):
    answer = []
    count = -1

    for i in range(len(num_list)):
        if i % n == 0:
            count += 1
            answer.append([])
        answer[count].append(num_list[i])

    return answer
