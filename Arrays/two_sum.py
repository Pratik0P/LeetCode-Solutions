# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    hashmap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i
