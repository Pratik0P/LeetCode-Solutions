# Problem: Kth Largest Element in an Array
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]
