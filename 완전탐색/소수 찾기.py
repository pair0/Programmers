# 시간 복잡도가 너무 크다.
from itertools import permutations


def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True  # 소수임


def solution(numbers):
    answer = 0
    setNumber = set()

    for j in range(1, len(numbers) + 1):
        for i in permutations(numbers, j):
            setNumber.add(int("".join(i)))

    for i in setNumber:
        if i > 1:
            if is_prime_number(i):
                answer += 1
    return answer
