# Problem: Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/

def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for n in nums:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest
