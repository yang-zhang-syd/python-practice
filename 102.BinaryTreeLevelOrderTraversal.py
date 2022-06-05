from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
        '''
        if not root:
            return []
        
        waitingList = [root, None]
        result = []
        currentLevel = []
        while len(waitingList) != 0:
            currentNode = waitingList.pop(0)
            if not currentNode:
                result.append(currentLevel)
                currentLevel = []
                if len(waitingList) > 0:
                    waitingList.append(None)
            else:
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    waitingList.append(currentNode.left)
                if currentNode.right:
                    waitingList.append(currentNode.right)
        
        return result
                