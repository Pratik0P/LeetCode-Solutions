# Problem: Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/

def numIslands(grid):
    if not grid:
        return 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                dfs(r, c)
                islands += 1

    return islands
