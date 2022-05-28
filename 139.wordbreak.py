from typing import collections, List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        if not s or len(s) == 0:
            return True
        
        dic = collections.Counter(wordDict)

        return self.wordBreakMem(s, dic, {})

    def wordBreakMem(self, s: str, dic, mem) -> bool:

        if not s or len(s) == 0:
            return True

        if s in mem:
            return mem[s]

        candidates = []
        for i in range(1, len(s) + 1):
            sub = s[:i]
            if sub in dic:
                candidates.append(sub)
        
        result = False
        for c in candidates:
            length = len(c)
            if self.wordBreakMem(s[length:], dic, mem):
                result = True
                break

        mem[s] = result

        return result


s = Solution()
print(s.wordBreak("aaaaaaa", ["aaaa","aaa"]))