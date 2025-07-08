# Problem: Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
