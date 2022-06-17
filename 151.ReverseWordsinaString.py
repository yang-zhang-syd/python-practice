class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        word = ''
        result = ''
        while i <= len(s):
            if i == len(s) or s[i] == ' ':
                if word != '':
                    result = word + ' ' + result if result != '' else word
                word = ''
            else:
                word += s[i]

            i += 1

        return result