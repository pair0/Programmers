def solution(balls, share):
    answer = 0
    num1 = 1  # 분자
    num2 = 1  # 분모

    for i in range(share):
        num1 *= (balls - i)
        num2 *= (share-i)

    answer = num1 / num2
    return answer
