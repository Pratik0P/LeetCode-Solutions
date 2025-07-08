# Problem: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/

def maxArea(height):
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        width = r - l
        max_area = max(max_area, width * min(height[l], height[r]))

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area
