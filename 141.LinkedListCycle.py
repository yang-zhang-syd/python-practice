from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}
        while head:
            if head in dic:
                return True
            else:
                dic[head] = 1
            head = head.next
        return False