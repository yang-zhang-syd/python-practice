class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        start1 = 0
        start2 = 0
        while start1 < len(version1) or start2 < len(version2):
            (num1, start1) = self.getNextNumber(version1, start1)
            (num2, start2) = self.getNextNumber(version2, start2)
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1

        return 0

    def getNextNumber(self, version: str, startIndex:int) -> (int, int):
        if startIndex >= len(version):
            return (0, startIndex)

        numStr = ''
        while startIndex < len(version):
            if version[startIndex] == '.':
                startIndex += 1
                break
            numStr += version[startIndex]
            startIndex += 1
        
        return (int(numStr), startIndex)