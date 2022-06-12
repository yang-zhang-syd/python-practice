# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        return root.left and self.pathSum(root.left, root.val, targetSum) or \
            root.right and self.pathSum(root.right, root.val, targetSum)

    def pathSum(self, currentNode: Optional[TreeNode], prevSum: int, targetSum: int) -> bool:
        
        prevSum += currentNode.val

        if not currentNode.left and not currentNode.right:
            return prevSum == targetSum
        
        return currentNode.left and self.pathSum(currentNode.left, prevSum, targetSum) or \
            currentNode.right and self.pathSum(currentNode.right, prevSum, targetSum)
        
