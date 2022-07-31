from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        m = len(forest)
        n = len(forest[0])
        total = m * n

        # (i,j) -> map((k,l))
        blocked = {}

        # (i, j) -> True/False
        visited = {}
        
        # return (steps, blocked)
        def cutTree(i, j, blocked, visited):
            
            nodeKey = f'{i}-{j}'

            visited[nodeKey] = True
            
            if forest[i][j] == 0:
                return 0, True

            blockedNodes = blocked[nodeKey] if nodeKey in blocked else {}

            # visit remaining none blocked nodes

            upJ = j + 1
            if upJ < n and f'{i}-{upJ}' not in blockedNodes:
                steps, isBlocked = cutTree(i, upJ, blocked, visited)
                if isBlocked:
                    blocked[nodeKey][f'{i}-{upJ}'] = True
            
            leftI = i - 1
            if leftI >= 0:
                cutTree(leftI, j, blocked, visited)

            rightI = i + 1
            if rightI < m:
                cutTree(rightI, j, blocked, visited)

            downJ = j - 1
            if downJ >= 0:
                cutTree(i, downJ, blocked, visited)

            remaining = total - len(visited)

            return 1

        return cutTree(0, 0, blocked, visited)