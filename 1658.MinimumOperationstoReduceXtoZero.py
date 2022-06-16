from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        total = sum(nums)
        target = total - x
        if target == 0:
            return len(nums)
            
        l= 0
        lrSum = 0
        maxLength = 0
        
        for r in range(len(nums)):
            
            lrSum += nums[r]
            
            while l <= r:
                
                if lrSum == target:
                    length = r - l + 1
                    if length > maxLength:
                        maxLength = length
                    break
                    
                elif lrSum > target:
                    lrSum -= nums[l]
                    l += 1
                else:
                    break

        return len(nums) - maxLength if maxLength != 0 else -1

s = Solution()
r = s.minOperations([1,1,4,3,2], 5)

print(r)