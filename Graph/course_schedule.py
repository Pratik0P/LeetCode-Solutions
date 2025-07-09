# Problem: Course Schedule
# Link: https://leetcode.com/problems/course-schedule/

from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    taken = 0

    while queue:
        course = queue.popleft()
        taken += 1
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return taken == numCourses
