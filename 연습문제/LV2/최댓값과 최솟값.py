def solution(s):
    s_list = sorted(map(int, s.split()))  # 각 원소를 int로 변경해서 비교
    print(s_list)
    answer = f'{s_list[0]} {s_list[-1]}'

    return answer
