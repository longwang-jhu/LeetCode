# https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take course
# ai.

# Return the ordering of courses you should take to finish all courses. If there
# are many valid answers, return any of them. If it is impossible to finish all
# courses, return an empty array.

################################################################################

# topological sort
# construct graph and get indegrees
# start from the node with indegree == 0

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        
        # construct graph and get indegrees
        graph = [[] for _ in range(n)] # graph: prereq -> [courses]
        node_indegree = [0] * n
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            node_indegree[course] += 1
        
        # bfs
        start_nodes = [node for node in range(n) if node_indegree[node] == 0]
        queue = collections.deque(start_nodes)
        ans = []
        
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for next in graph[curr]:
                node_indegree[next] -= 1
                if node_indegree[next] == 0:
                    queue.append(next)

        return ans if len(ans) == n else []
