def solution(my_string):
    answer = 0
    temp = ''

    for s in my_string:
        if ord(s) >= 65:
            if temp != '':
                answer += int(temp)
                temp = ''
            continue
        else:
            temp += s

    # 숫자가 맨 마지막에 올 때
    if temp != '':
        answer += int(temp)
    return answer
