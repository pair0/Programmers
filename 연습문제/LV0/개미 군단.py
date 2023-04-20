def solution(hp):
    answer = 0

    answer += hp//5
    hp = hp - ((hp//5)*5)
    answer += hp//3
    hp = hp - ((hp//3)*3)
    answer += hp//1
    hp = hp - ((hp//1)*1)

    return answer
