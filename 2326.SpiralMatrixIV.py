from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        ans = []
        for i in range(m):
            ans.append([-1] * n)

        if not head:
            return ans

        i = 0 
        j = m - 1
        x = i

        k = 0
        l = n - 1
        y = k

        dir = 0 # 0 - left to right, 1 - right to left, 2 - up to down, 3 - down to up

        ans[0][0] = head.val
        head = head.next

        count = 1
        while count < m * n and head:

            if dir == 0:
                y += 1
                if y == l + 1:
                    dir = 2
                    i += 1
                    y = l
                    continue

            elif dir == 1:
                y -= 1
                if y == k - 1:
                    dir = 3
                    j -= 1
                    y = k
                    continue
            elif dir == 2:
                x += 1
                if x == j + 1:
                    dir = 1
                    l -= 1
                    x = j
                    continue
            elif dir == 3:
                x -= 1
                if x == i - 1:
                    dir = 0
                    x = i
                    k += 1
                    continue

            ans[x][y] = head.val
            head = head.next
            count += 1
        
        return ans