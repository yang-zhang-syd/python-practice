from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ans = []
        for i in range(n):
            ans.append([0] * n)

        nums = [0] * (n * n)
        for idx, val in enumerate(range(1, n*n + 1)):
            nums[idx] = val
        
        i = 0 
        j = n - 1
        x = i

        k = 0
        l = n - 1
        y = k

        dir = 0 # 0 - left to right, 1 - right to left, 2 - up to down, 3 - down to up

        ans[x][y] = nums[0]

        m = 1
        while m < n * n:

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
            
            ans[x][y] = nums[m]

            m += 1

        return ans

s = Solution()
s.generateMatrix(3)