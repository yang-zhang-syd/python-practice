from typing import *

class TrieNode:
    def __init__(self) -> None:   
        self.value = '' 
        self.word = ''
        self.children = [None] * 26
        self.eow = False

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str):
        if not word:
            return
        
        currentNode = self.root

        for c in word:
            if currentNode.children[ord(c) - ord('a')]:
                currentNode = currentNode.children[ord(c) - ord('a')]
            else:
                newNode = TrieNode()
                currentNode.children[ord(c) - ord('a')] = newNode
                currentNode = newNode
                currentNode.value = c

        currentNode.eow = True
        currentNode.word = word
    
    def search(self, node: TrieNode, c: str) -> TrieNode:
        if not node:
            return None
        
        if node.children[ord(c) - ord('a')]:
            return node.children[ord(c) - ord('a')]
        
        return None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()

        for word in words:
            trie.add(word)

        result = set()
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if trie.root.children[self.trieIndex(cell)]:
                    visitedSet = set()
                    self.findWord_Recursive(trie.root.children[self.trieIndex(cell)], board, i, j, result, visitedSet)

        return list(result)

    def findWord_Recursive(self, node: TrieNode, board, i, j, result: set, visitedSet):

        key = str(i) + ',' + str(j)
        if key in  visitedSet:
            return False
        else:
            visitedSet.add(key)

        if node.eow:
            result.add(node.word)

        for k, l in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
            if k < 0 or k > len(board) - 1 or l < 0 or l > len(board[0]) - 1:
                continue
            c = board[k][l]
            nextNode = node.children[self.trieIndex(c)]
            if nextNode:
                self.findWord_Recursive(nextNode, board, k, l, result, visitedSet)
                if nextNode.eow and nextNode.word in result and not any(nextNode.children):
                    node.children[self.trieIndex(c)] = None
        
        visitedSet.remove(key)

    def trieIndex(self, c) -> int:
        return ord(c) - ord('a')
        

s = Solution()
r = s.findWords([["a","b","c"],["a","e","d"],["a","f","g"]], \
["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"])

print(r)