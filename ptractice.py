class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max = (0, 0)
        prev = {}
        for n in range(len(s)):
            if n % 2 == 0:
                p = {}
            for i in range(len(s)):
                j = i + n
                if j >= len(s):
                    break
                k = i + 1
                l = j - 1
                if k >= l:
                    p[str(i)+','+str(j)] = s[i] == s[j]

                else:
                    p[str(i)+','+str(j)] = prev[str(k)+','+str(l)] and s[i] == s[j]
                    
                if p[str(i)+','+str(j)]:
                    length = j - i + 1
                    if length > max[1] - max[0] + 1:
                        max = (i, j)
            if n % 2 == 1:
                prev = p

        return s[max[0]:max[1]+1]


s = Solution()
r = s.longestPalindrome("abcba")
print(r)