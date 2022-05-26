from typing import List
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # setup connections between words
        dic = {}
        nodesDic = {}
        nodes = map(lambda x: [x, False, 0, False, None, []], wordList)
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
        connected = self.findConnectedWords([beginWord, False, 0, False, None, []], dic, 1, endWord)
        paths = []
        while connected:
            first = connected.pop(0)
            first[1] = True
            level = first[2]
            if len(paths) > 0 and len(paths[0]) < level:
                break
            if first[0] == endWord:
                paths.append(first[5] + [first[0]])

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
                    if not candidate[1] and candidate[0] != word and (not candidate[3] or candidate[0] == endWord):
                        candidate[2] = level
                        candidate[3] = True
                        candidate[5] = node[5] + [word]
                        candidate[4] = node
                        candidates.append(candidate)
        return candidates

s = Solution()
r = s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
print(r)
