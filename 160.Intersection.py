from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        while headA and headB:
            if headA and headA in visited:
                return headA
            elif headA:
                visited.add(headA)
                headA = headA.next
            if headB and headB in visited:
                return headB
            elif headB:
                visited.add(headB)
                headB = headB.next
        
        return None