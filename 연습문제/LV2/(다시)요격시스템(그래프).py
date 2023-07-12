def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    end = -1  # 마지막으로 요격한 미사일의 x좌표

    for s, e in targets:
        # 이전에 요격한 미사일로는 현재 미사일을 요격할 수 없는 경우
        if s > end:
            answer += 1
            end = e - 1  # 현재 미사일을 요격함으로써 끝나는 지점을 업데이트, 개구간이므로 -1

    return answer
