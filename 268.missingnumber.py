from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = {nums[0]: True}
        maxNum = nums[0]
        for num in nums[1:]:
            if num > maxNum:
                maxNum = num
            dic[num] = True
        
        for i in range(maxNum + 1):
            if i not in dic:
                return i
            
        return maxNum + 1

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actualSum = 0
        nSum = 0
        for i in range(n + 1):
            nSum += i
            if i <= n - 1:
                actualSum += nums[i] 

        return nSum - actualSum