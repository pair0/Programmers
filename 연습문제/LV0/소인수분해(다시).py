def solution(n):
    answer = set()  # 소인수 분해한 결과를 저장할 리스트
    i = 2  # 가장 작은 소수인 2부터 시작
    while i <= n:
        if n % i == 0:  # n이 i로 나누어 떨어지면
            answer.add(i)  # i를 소인수로 추가
            n //= i  # n을 i로 나눈 몫을 새로운 n으로 설정
        else:
            i += 1  # i를 1 증가시킴
    return sorted(list(answer))
