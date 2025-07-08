# Problem: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
