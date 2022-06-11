# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        currentLevel = [root]
        nextLevel = []
        
        while len(currentLevel) != 0 or len(nextLevel) != 0:
            if len(currentLevel) == 0:
                currentLevel = nextLevel
                nextLevel = []
                continue
            if len(currentLevel) == 1:
                node = currentLevel.pop()
                idx = len(nextLevel) // 2
                nextLevel.insert(idx, node.left)
                nextLevel.insert(idx + 1, node.right)
                continue
            front = currentLevel.pop(0)
            end = currentLevel.pop()
            if front and not end or not front and end:
                return False
            if not front and not end:
                continue
            if front.val != end.val:
                return False
            idx = len(nextLevel) // 2
            nextLevel.insert(idx, front.left)
            nextLevel.insert(idx + 1, front.right)
            nextLevel.insert(idx + 2, end.left)
            nextLevel.insert(idx + 3, end.right)

        return True