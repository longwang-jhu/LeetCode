# https://leetcode.com/problems/course-schedule/

# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.

# Return true if you can finish all courses. Otherwise, return false.

###############################################################################

# topological sort
# construct graph[course] = [child1, ...] and get indegrees[course]
# start from the node with indegree == 0

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        
        # construct graph and get indegrees
        graph = [[] for _ in range(n)] # graph: prereq -> [courses]
        indegree = [0] * n
        for child, course in prerequisites:
            graph[course].append(child)
            indegree[child] += 1
        
        # bfs
        queue = deque([node for node in range(n) if indegree[node] == 0])
        count = 0 # number of courses taken
        while queue:
            curr = queue.popleft()
            count += 1
            for child in graph[curr]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        return count == n