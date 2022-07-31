from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        # i = 0, j = m - 1, i >= j
        # k = 0, l = n - 1, k >= l

        ans = [matrix[0][0]]

        i = 0 
        j = m - 1
        x = i

        k = 0
        l = n - 1
        y = k

        dir = 0 # 0 - left to right, 1 - right to left, 2 - up to down, 3 - down to up

        while len(ans) != m * n:

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
            
            ans.append(matrix[x][y])

        return ans

s = Solution()
#s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
s.spiralOrder([[1,2,3]])
