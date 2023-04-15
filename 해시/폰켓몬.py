def solution(nums):
    choose = len(nums) / 2
    nums = set(nums)
    answer = min(len(nums), choose)
    return answer
