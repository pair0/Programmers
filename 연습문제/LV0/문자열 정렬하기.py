def solution(my_string):
    # lower()로 소문자로 변환, sorted로 정렬, 정렬을 진행하면 리스트로 변환되기 때문에 join으로 string형태로 다시 변환
    answer = "".join(sorted(my_string.lower()))
    return answer
