# Problem: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
    max_sum = curr_sum = nums[0]
    for n in nums[1:]:
        curr_sum = max(n, curr_sum + n)
        max_sum = max(max_sum, curr_sum)
    return max_sum
