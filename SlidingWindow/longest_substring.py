# Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    char_set = set()
    l = 0
    result = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        result = max(result, r - l + 1)
    return result
