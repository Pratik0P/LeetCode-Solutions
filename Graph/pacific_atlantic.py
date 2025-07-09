# Problem: Pacific Atlantic Water Flow
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

def pacificAtlantic(heights):
    if not heights:
        return []

    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visited, prev_height):
        if ((r, c) in visited or
            r < 0 or c < 0 or r >= ROWS or c >= COLS or
            heights[r][c] < prev_height):
            return
        visited.add((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, visited, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])

    return list(pac & atl)
