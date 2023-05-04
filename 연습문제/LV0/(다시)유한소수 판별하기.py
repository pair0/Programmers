def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def solution(a, b):
    answer = 0
    # 분모를 기약분수로 나타내기 (분모를 분자와 분모의 최대공약수로 나눈다.)
    b //= gcd(a, b)

    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    if b == 1:
        answer = 1
    else:
        answer = 2

    return answer
