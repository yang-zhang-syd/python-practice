from typing import *

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        ans = []
        if rows == 0 or cols == 0:
            return ans

        y = rStart
        x = cStart

        dir = 0 # 0 - left to right, 1 - right to left, 2 - up to down, 3 - down to up

        leftBound = cStart # left boundary
        rightBound = cStart + 1 # right boundary
        topBound = rStart # top boundary
        bottomBound = rStart # bottom boundary
        
        ans.append([y, x])

        while len(ans) < rows * cols:
            if dir == 0:
                x += 1
                if x > rightBound:
                    x = rightBound
                    dir = 2
                    bottomBound += 1
                    continue
            elif dir == 1:
                x -= 1
                if x < leftBound:
                    x = leftBound
                    dir = 3
                    topBound -= 1
                    continue
            elif dir == 2:
                y += 1
                if y > bottomBound:
                    y = bottomBound
                    dir = 1
                    leftBound -= 1
                    continue
            elif dir == 3:
                y -= 1
                if y < topBound:
                    y = topBound
                    dir = 0
                    rightBound += 1
                    continue
            
            if x >= 0 and x < cols and y >= 0 and y < rows:
                ans.append([y, x])
        
        return ans
            
s = Solution()
s.spiralMatrixIII(1, 4, 0, 0)