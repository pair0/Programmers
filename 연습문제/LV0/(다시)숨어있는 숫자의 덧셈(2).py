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


# 더 나은 풀이
def solution(my_string):
    for i in my_string:
        if i.isalpha():  # 알파벳일 때 공백으로 변환
            my_string = my_string.replace(i, ' ')
    my_string = my_string.split()  # 공백 기준으로 자르기

    return sum(list(map(int, my_string)))
