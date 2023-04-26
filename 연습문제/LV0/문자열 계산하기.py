def solution(my_string):
    answer = 0
    my_list = my_string.split()

    for i in range(len(my_list)):
        if i == 0:
            answer = int(my_list[i])
        elif my_list[i] == '+':
            answer += int(my_list[i+1])
        elif my_list[i] == '-':
            answer -= int(my_list[i+1])
    return answer
