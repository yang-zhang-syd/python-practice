from typing import *

class TrieNode:
    def __init__(self) -> None:    
        self.value = ''
        self.children = [None] * 26
        self.leaf = False

class Trie:
    root = TrieNode()

    def add(self, word: str):
        if not word:
            return
        
        currentNode = self.root

        for c in word:
            if currentNode.children[ord(c) - ord('a')]:
                currentNode = currentNode.children[ord(c) - ord('a')]
            else:
                newNode = TrieNode()
                newNode.value = c
                currentNode.children[ord(c) - ord('a')] = newNode
                currentNode = newNode

        currentNode.leaf = True
    
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

        return []

s = Solution()
s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])