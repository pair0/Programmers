# 지도 1 벽 or 지도 2 벽 => 벽 #
# 지도 1 공백 and 지도 2 공백 => 공백 " "


def solution(n, arr1, arr2):
    answer = ["" for _ in range(n)]

    for i in range(n):
        a1 = format(arr1[i], "b").zfill(n)
        a2 = format(arr2[i], "b").zfill(n)
        for j in range(n):
            if a1[j] == "1" or a2[j] == "1":
                answer[i] += "#"
            elif a1[j] == "0" and a2[j] == "0":
                answer[i] += " "

    return answer
