# https://leetcode.com/problems/shortest-bridge/

# In a given 2D binary array A, there are two islands.  (An island is a
# 4-directionally connected group of 1s not connected to any other 1s.)

# Now, we may change 0s to 1s so as to connect the two islands together to form
# 1 island.

# Return the smallest number of 0s that must be flipped.  (It is guaranteed
# that the answer is at least 1.)

###############################################################################

# use dfs to find first island
# use bfs to reach for second island

from collections import deque
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.m, self.n = len(A), len(A[0])
        self.A = A
        self.dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        self.queue = deque()
        
        # search for the first island
        found_1st = False
        for i in range(self.m):
            if found_1st: break
            for j in range(self.n):
                if self.A[i][j] == 1:
                    self.dfs(i,j)
                    found_1st = True
                    break # break out all loops
        
        # expand to the second island
        ans = 0
        while self.queue:
            curr_len = len(self.queue)
            for _ in range(curr_len):
                i, j = self.queue.popleft()
                for dir_idx in range(4):
                    i_next = i + self.dirs[dir_idx][0]
                    j_next = j + self.dirs[dir_idx][1]
                    if (0 <= i_next < self.n and 0 <= j_next < self.m
                        and self.A[i_next][j_next] != -1):
                        if self.A[i_next][j_next] == 1: # reach the new island
                            return ans
                        
                        if self.A[i_next][j_next] == 0: # flip the land
                            self.queue.append((i_next, j_next))
                            self.A[i_next][j_next] = -1
            ans += 1
            
    def dfs(self, i, j):
        if self.A[i][j] == 0:
            return
        self.queue.append((i,j)) # add to queue
        self.A[i][j] = -1 # mark for visited
        
        for dir_idx in range(4):
            i_next = i + self.dirs[dir_idx][0]
            j_next = j + self.dirs[dir_idx][1]
            if (0 <= i_next < self.n and 0 <= j_next < self.m
                and self.A[i_next][j_next] != -1):
                self.dfs(i_next, j_next)