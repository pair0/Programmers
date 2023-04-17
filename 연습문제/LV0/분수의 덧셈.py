import math


def solution(numer1, denom1, numer2, denom2):
    answer = []

    plus_denom = denom1 * denom2
    plus_numer = (numer1 * denom2) + (numer2 * denom1)
    divi = math.gcd(plus_numer, plus_denom)  # 분모와 분자의 최대공약수

    answer = [plus_numer/divi, plus_denom/divi]

    return answer
