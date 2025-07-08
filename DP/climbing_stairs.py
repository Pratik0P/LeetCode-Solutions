# Problem: Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/

def climbStairs(n):
    if n <= 2:
        return n
    first = 1
    second = 2
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second
