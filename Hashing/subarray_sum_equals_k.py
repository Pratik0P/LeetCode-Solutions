# Problem: Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k/

def subarraySum(nums, k):
    count = 0
    curr_sum = 0
    hashmap = {0: 1}

    for n in nums:
        curr_sum += n
        count += hashmap.get(curr_sum - k, 0)
        hashmap[curr_sum] = hashmap.get(curr_sum, 0) + 1

    return count
