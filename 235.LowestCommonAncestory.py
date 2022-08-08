# Definition for a binary tree node.
from turtle import right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        rst = self.find(root, p, q)

        return rst[2]

    def find(self, root, p, q):

        pFound = True if root == p else False
        qFound = True if root == q else False

        leftPFound = False
        leftQFound = False
        leftFound = None
        if root.left:
            (leftPFound, leftQFound, leftFound) = self.find(root.left, p, q)
            if leftPFound and leftQFound:
                return (leftPFound, leftQFound, leftFound)

        rightPFound = False
        rightQFound = False
        rightFound = None
        if root.right:
            (rightPFound, rightQFound, rightFound) = self.find(root.right, p, q)
            if rightPFound and rightQFound:
                return (rightPFound, rightQFound, rightFound)
        
        if leftPFound and rightQFound \
            or leftQFound and rightPFound \
            or leftPFound and root == q \
            or rightPFound and root == q \
            or leftQFound and root == p \
            or rightQFound and root == p:
            return (True, True, root)
        
        return (pFound or leftPFound or rightPFound, qFound or rightQFound or leftQFound, None)

    