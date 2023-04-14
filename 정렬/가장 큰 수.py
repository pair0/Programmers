def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 4, reverse=True)

    # '0000'의 경우를 '0'으로 만들기 위해 int로 치환 후, str 재 치환
    return str(int(''.join(numbers)))
