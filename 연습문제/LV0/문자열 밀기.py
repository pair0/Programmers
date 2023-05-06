def solution(A, B):
    answer = 0
    length = len(A)

    for i in range(0, length+1):
        temp = ''
        temp += A[length-i:]
        temp += A[:length-i]

        if temp == B:
            return i

    return -1
