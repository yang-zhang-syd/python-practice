from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum_rec(root)
        
        return self.max_sum

    def max_sum_rec(self, node: Optional[TreeNode]) -> int:
        
        if not node:
            return 0

        maxLeft = self.max_sum_rec(node.left)
        maxRight = self.max_sum_rec(node.right)

        sum = node.val + maxLeft + maxRight
        leftSum = node.val + maxLeft
        rightSum = node.val + maxRight
        
        max_sum_local = max(sum, leftSum, rightSum, node.val)

        if max_sum_local > self.max_sum:
            self.max_sum = max_sum_local

        return max(leftSum, rightSum, node.val)
