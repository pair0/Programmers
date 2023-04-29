def solution(sides):
    answer = 0
    sides.sort()

    # 가장 긴 변이 매개변수인 경우
    answer += (sides[1] - (sides[1] - sides[0]) - 1)

    # 가장 긴 변이 매개변수가 아닌 경우
    answer += (sum(sides) - sides[1])
    return answer
