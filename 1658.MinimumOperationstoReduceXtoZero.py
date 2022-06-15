from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        total = sum(nums)
        if total == x:
            return len(nums)
        
        target = total - x

        l= 0
        r = 0
        lrSum = nums[0]
        maxLength = 0

        while r < len(nums):
            if lrSum == target:
                length = r - l + 1
                if length > maxLength:
                    maxLength = length
                r += 1
                lrSum += nums[r] if r < len(nums) else 0
            elif lrSum < target:
                r += 1
                lrSum += nums[r] if r < len(nums) else 0
            else:
                lrSum -= nums[l]
                l += 1
                if l > r:
                    r += 1
                    lrSum += nums[r] if r < len(nums) else 0

        return len(nums) - maxLength if maxLength != 0 else -1

s = Solution()
r = s.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365)

print(r)