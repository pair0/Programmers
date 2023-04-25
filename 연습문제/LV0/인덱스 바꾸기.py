def solution(my_string, num1, num2):
    temp1 = my_string[num1]
    temp2 = my_string[num2]
    my_string = list(my_string)
    my_string[num1] = temp2
    my_string[num2] = temp1
    answer = ''.join(my_string)
    return answer
