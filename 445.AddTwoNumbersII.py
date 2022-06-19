from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        
        num2 = 0
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        
        result = num1 + num2

        tail = ListNode(result % 10)
        result = result // 10

        while result != 0:
            head = ListNode(result % 10)
            head.next = tail
            tail = head
            result = result // 10
        
        return tail

s = Solution()
r = s.addTwoNumbers([7,2,4,3],[5,6,4])
print(r.val)