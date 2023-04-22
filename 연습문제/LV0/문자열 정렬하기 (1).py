def solution(my_string):
    answer = []
    number = [str(i) for i in range(10)]

    for i in my_string:
        if i in number:
            answer.append(int(i))

    answer.sort()

    return answer
