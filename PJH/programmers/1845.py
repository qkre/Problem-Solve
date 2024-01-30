def solution(nums):
    answer = 0
    max_diverse = len(nums) // 2

    nums = set(nums)

    if max_diverse > len(nums):
        return len(nums)

    return max_diverse
