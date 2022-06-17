class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while i < len(s):
            s.insert(0, s[i])
            s.pop(i+1)
            i += 1