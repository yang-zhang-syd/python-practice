from typing import List
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # setup connections between words
        dic = {}
        nodesDic = {}
        nodes = map(lambda x: [x, False, 0, False], wordList)
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
        current = beginWord
        connected = self.findConnectedWords(current, dic, 1)
        while connected:
            first = connected.pop(0)
            first[1] = True
            l = first[2]
            if first[0] == endWord:
                return first[2] + 1
            else:
                connected1 = self.findConnectedWords(first[0], dic, l + 1)
                connected += connected1

        return 0

    def findConnectedWords(self, word, dic, level):
        candidates = []
        for i in range(len(word)):
            key = word[:i] + '*' + word[i+1:]
            if key in dic:
                for candidate in dic[key]:
                    if not candidate[1] and candidate[0] != word and not candidate[3]:
                        candidate[2] = level
                        candidate[3] = True
                        candidates.append(candidate)
        return candidates

s = Solution()
r = s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
print(r)
