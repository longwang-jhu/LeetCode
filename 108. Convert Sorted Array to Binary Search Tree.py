# divide and conquer
# pick mid as node, node.left = build_tree(left), node.right = build_tree(right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build_tree(nums, 0, len(nums) - 1)
   
    def build_tree(self, nums, left, right):
        if left > right:
            return None
        
        mid = left + (right - left) // 2
        node = TreeNode(nums[mid])
        node.left = self.build_tree(nums, left, mid - 1)
        node.right = self.build_tree(nums, mid + 1, right)
        return node