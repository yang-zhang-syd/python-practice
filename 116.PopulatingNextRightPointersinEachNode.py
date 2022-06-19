from typing import Optional, List

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        
        if not root:
            return
        
        firstLevel = [root]
        self.connectRecursive(firstLevel)
        return root

    def connectRecursive(self, nodes: List[Node]) -> None:

        nextLevel = []
        length = len(nodes)
        
        if length == 0:
            return

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
            if nodes[i].left:
                nextLevel.append(nodes[i].left)
            if nodes[i].right:
                nextLevel.append(nodes[i].right)

        if nodes[length - 1].left:
            nextLevel.append(nodes[length - 1].left)
        if nodes[length - 1].right:
            nextLevel.append(nodes[length - 1].right)
        
        self.connectRecursive(nextLevel)