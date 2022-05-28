from typing import List
import collections

class Node:

    visited = False
    value = ''
    level = 0
    inWaitingList = False
    path = []

    def __init__(self, val):
        self.value = val
    
class Solution:
    '''
    BFS
    1. If a node in the graph was visited, 
    '''
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # setup connections between words
        dic = {}
        nodesDic = {}
        nodes = map(lambda x: Node(x), wordList)
        for node in nodes:
            nodesDic[node.value] = node
        
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                if key in dic:
                    dic[key].append(nodesDic[word]) # word and visited flag as dictionary value
                else:
                    dic[key] = [nodesDic[word]]
                
        # search for end word
        count = 0
        connected = self.findConnectedWords(Node(beginWord), dic, 1, endWord)
        paths = []
        while connected:
            first = connected.pop(0)
            first.visited = True
            level = first.level
            if len(paths) > 0 and len(paths[0]) <= level:
                break
            if first.value == endWord:
                paths.append(first.path + [first.value])

            connected1 = self.findConnectedWords(first, dic, level + 1, endWord)
            connected += connected1

        return paths

    def findConnectedWords(self, node, dic, level, endWord):
        word = node.value
        candidates = []
        for i in range(len(word)):
            key = word[:i] + '*' + word[i+1:]
            if key in dic:
                for candidate in dic[key]:
                    if not candidate.visited and candidate.value != word and not candidate.inWaitingList:
                        candidate.level = level
                        candidate.inWaitingList = True
                        candidate.path = node.path + [word]
                        candidates.append(candidate)
                    elif not candidate.visited and candidate.value != word and candidate.inWaitingList:
                        # this is the end node and it was added to the waiting list before
                        toAdd = Node(candidate.value)
                        toAdd.visited = True
                        toAdd.level = level
                        toAdd.inWaitingList = True
                        toAdd.path = node.path + [word]
                        candidates.append(toAdd)
        return candidates

s = Solution()
r = s.findLadders('a', 'c', ["a","b","c"])
print(r)
