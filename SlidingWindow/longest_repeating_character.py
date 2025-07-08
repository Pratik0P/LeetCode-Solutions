# Problem: Longest Repeating Character Replacement
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

def characterReplacement(s, k):
    count = {}
    res = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_freq = max(count.values())

        while (r - l + 1) - max_freq > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res
