# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        
        if root:
            self.inorderRecur(root, output)
        
        return output
        
        
    def inorderRecur(self, root: Optional[TreeNode], output: List[int]) -> None:
        
        if root.left:
            self.inorderRecur(root.left, output)
        
        output.append(root.val)
        
        if root.right:
            self.inorderRecur(root.right, output)