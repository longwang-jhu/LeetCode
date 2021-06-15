# https://leetcode.com/problems/jump-game-iii/

# Given an array of non-negative integers arr, you are initially positioned at
# start index of the array. When you are at index i, you can jump to i + arr[i] or
# i - arr[i], check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.

################################################################################

# use stack to record path
# use set to record visited pos

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        if n == 1:
            return arr[0] == 0
        
        stack = [start]
        visited = set([start]) # record visited pos
        
        while stack:
            curr = stack.pop()
            if arr[curr] == 0:
                return True
            
            # go left
            left = curr - arr[curr]
            if 0 <= left < n and left not in visited:
                visited.add(left)
                stack.append(left)
            
            # go right
            right = curr + arr[curr]
            if 0 <= right < n and right not in visited:
                visited.add(right)
                stack.append(right)
        
        return False
