# DFS, add larger numbers as child

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        
        def subsets_dfs(pos):
            ans.append(path.copy())
            for i in range(pos, n):
                path.append(nums[i])
                subsets_dfs(i + 1)
                path.pop()

        subsets_dfs(0);
        return ans