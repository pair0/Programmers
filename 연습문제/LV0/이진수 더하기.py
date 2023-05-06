# ### 런타임 에러
# def solution(bin1, bin2):
#     answer = ''
#     value = 0
#     plus = 0

#     for i in range(max(len(bin1), len(bin2))-1, -1, -1):
#         value = int(bin1[i]) + int(bin2[i]) + plus
#         if value > 1:
#             answer += str(value - 2)
#             plus = 1
#         else:
#             answer += str(value)
#             plus = 0

#     if plus == 1:
#         answer += '1'

#     return answer[::-1]

# 이게 맞음
def solution(bin1, bin2):
    bin1 = int(bin1, 2)
    bin2 = int(bin2, 2)
    answer = bin(bin1+bin2)

    return answer[2:]
