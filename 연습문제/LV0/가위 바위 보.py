def solution(rsp):
    answer = ''

    for i in rsp:
        if i == '2':  # 가위를 냈을 때
            answer += '0'
        elif i == '0':  # 바위를 냈을 때
            answer += '5'
        else:  # 보를 냈을 때
            answer += '2'

    return answer
