from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reversed = s.reverse()

        begin = 0
        end = 0
        while end <= len(s):
            if s[end] == ' ' or end == len(s):
                self.reverseWord(s, begin, end - 1)
                begin = end + 1
                end = end + 1
            else:
                end += 1

    def reverseWord(self, s: List[str], begin: int, end: int) -> None:

        while begin < end:
            temp = s[begin]
            s[begin] = s[end]
            s[end] = temp
            begin += 1
            end -= 1