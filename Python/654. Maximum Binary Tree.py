# https://leetcode.com/problems/maximum-binary-tree/

# You are given an integer array nums with no duplicates. A maximum binary tree
# can be built recursively from nums using the following algorithm:

# Return the maximum binary tree built from nums.

###############################################################################

# divide and conquer
# find the maximum index

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct_tree(nums, 0, len(nums) - 1)
        
    def construct_tree(self, nums, left, right):
        if left == right:
            return TreeNode(nums[left])
        if left > right:
            return None
        
        sub_list = nums[left:right + 1]
        max_idx = sub_list.index(max(sub_list)) + left # get the index of the maximum in the original num
        
        node = TreeNode(nums[max_idx])
        node.left = self.construct_tree(nums, left, max_idx - 1)
        node.right = self.construct_tree(nums, max_idx + 1, right)
        
        return node