# Problem: Majority Element
# Link: https://leetcode.com/problems/majority-element/

def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
