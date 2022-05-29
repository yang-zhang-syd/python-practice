class Solution:
    def myAtoi(self, s: str) -> int:
        
        if not s or len(s) == 0:
            return 0
        
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        negative = False
        if i < len(s) and s[i] == '-':
            negative = True
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1

        j = i
        while j < len(s) and s[j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            j += 1

        s = s[i:j]

        if len(s) > 0:
            result = int(s)
        else:
            result = 0

        if negative:
            result = -result
            if result < -2** 31:
                result = -2**31
        elif result > 2**31 - 1:
            result = 2 ** 31 - 1

        return result

s = Solution()
print(s.myAtoi('  -123 abc'))