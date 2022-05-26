from typing import List
import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # setup connections between words
        dic = {}
        nodesDic = {}
        # node[0] : word
        # node[1] : visited flag
        # node[2] : level in BFS
        # node[3] : node added to connected array
        # node[4] : path from begin word
        nodes = map(lambda x: [x, False, 0, False, []], wordList)
        for node in nodes:
            nodesDic[node[0]] = node
        
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                if key in dic:
                    dic[key].append(nodesDic[word]) # word and visited flag as dictionary value
                else:
                    dic[key] = [nodesDic[word]]
                
        # search for end word
        count = 0
        connected = self.findConnectedWords([beginWord, False, 0, False, []], dic, 1, endWord)
        paths = []
        while connected:
            first = connected.pop(0)
            first[1] = True
            level = first[2]
            if len(paths) > 0 and len(paths[0]) <= level:
                break
            if first[0] == endWord:
                paths.append(first[4] + [first[0]])

            connected1 = self.findConnectedWords(first, dic, level + 1, endWord)
            connected += connected1

        return paths

    def findConnectedWords(self, node, dic, level, endWord):
        word = node[0]
        candidates = []
        for i in range(len(word)):
            key = word[:i] + '*' + word[i+1:]
            if key in dic:
                for candidate in dic[key]:
                    if not candidate[1] and candidate[0] != word and not candidate[3]:
                        candidate[2] = level
                        candidate[3] = True
                        candidate[4] = node[4] + [word]
                        candidates.append(candidate)
                    elif not candidate[1] and candidate[0] != word and candidate[3]:
                        # this is the end node and it was added to the waiting list before
                        candidates.append([candidate[0], candidate[1], level, True, node[4] + [word]])
        return candidates

s = Solution()
r = s.findLadders('a', 'c', ["a","b","c"])
print(r)
