def solution(quiz):
    answer = []

    for i in quiz:
        i_list = i.split()
        if i_list[1] == '+':
            if int(i_list[0]) + int(i_list[2]) == int(i_list[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(i_list[0]) - int(i_list[2]) == int(i_list[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer
