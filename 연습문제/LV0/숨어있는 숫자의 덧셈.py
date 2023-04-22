def solution(my_string):
    answer = 0
    number = [str(i) for i in range(10)]

    for i in my_string:
        if i in number:
            answer += int(i)

    return answer
