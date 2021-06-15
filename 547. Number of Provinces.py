# https://leetcode.com/problems/number-of-provinces/

# There are n cities. Some of them are connected, while some are not. If city a is
# connected directly with city b, and city b is connected directly with city c,
# then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith
# city and the jth city are directly connected, and isConnected[i][j] = 0
# otherwise.

# Return the total number of provinces.

################################################################################

# dfs -> generate child based on friends

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or not isConnected[0]: return 0
        
        self.n = len(isConnected)
        self.is_connected = isConnected
        self.visited = set()
        ans = 0
        for i in range(self.n):
            if i not in self.visited:
                self.dfs(i)
                ans += 1
        return ans
    
    def dfs(self, i):
        self.visited.add(i)
        # generate children
        for j in range(self.n):
            if j != i and j not in self.visited and self.is_connected[i][j] == 1:
                self.dfs(j)
