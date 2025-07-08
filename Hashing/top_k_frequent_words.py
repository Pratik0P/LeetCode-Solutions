# Problem: Top K Frequent Words
# Link: https://leetcode.com/problems/top-k-frequent-words/

from collections import Counter
import heapq

def topKFrequent(words, k):
    count = Counter(words)
    return heapq.nsmallest(k, count, key=lambda x: (-count[x], x))
