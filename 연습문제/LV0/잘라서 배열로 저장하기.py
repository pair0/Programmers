def solution(my_str, n):
    answer = []

    for i in range(len(my_str)):
        if i % n == 0:
            answer.append([])
            str = ""
        str += my_str[i]
        answer[i//n] = str
    return answer
