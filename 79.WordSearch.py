from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board or not word:
            return False

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == word[0]:
                    visitedSet = set()
                    if self.search(i, j, board, word, visitedSet):
                        return True

        return False
    
    def search(self, i, j, board, word, visited) -> bool:

        if not word:
            return True

        if word[0] != board[i][j]:
            return False

        key = str(i) + ',' + str(j)
        if key in  visited:
            return False
        else:
            visited.add(key)

        if len(word) == 1:
            return True

        if i > 0 and self.search(i - 1, j, board, word[1:], visited):
            return True

        if j < len(board[i]) - 1 and self.search(i, j + 1, board, word[1:], visited):
            return True

        if i < len(board) - 1 and self.search(i + 1, j, board, word[1:], visited):
            return True

        if j > 0 and self.search(i, j - 1, board, word[1:], visited):
            return True

        visited.remove(key)

        return False

s = Solution()
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCEFSADEESE"))

# [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# "ABCEFSADEESE"