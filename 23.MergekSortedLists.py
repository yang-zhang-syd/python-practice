# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        q = PriorityQueue()

        for i, l in enumerate(lists):
            if l:
                q.put((l.val, i, l))

        result = point = ListNode(0)
        while not q.empty():
            val, idx, min = q.get()
            point.next = min
            point = min
            min = min.next
            if min:
                q.put((min.val, idx, min))
        
        return result.next