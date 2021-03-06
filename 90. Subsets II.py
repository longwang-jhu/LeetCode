# DFS: sort first, add child only when it is different than the previous

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        path = []
        
        def subsets_dfs(pos):
            ans.append(path.copy())
            for i in range(pos, n):
                if i != pos and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                subsets_dfs(i + 1)
                path.pop()

        subsets_dfs(0);
        return ans