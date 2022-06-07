from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        length = len(nums)

        closest = nums[0] + nums[1] + nums[2]
        minDiff = abs(target - closest)

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            pivot = nums[i]
            j = i + 1
            k = length - 1
            while j < k:
                sum = nums[j] + nums[k] + pivot
                diff = abs(target - sum)
                
                if target - sum == 0:
                    return sum

                if diff < minDiff:
                    closest = nums[i] + nums[j] + nums[k]
                    minDiff = diff
                
                if target - sum > 0:
                    j += 1
                else:
                    k += 1

        return closest

s = Solution()
print(s.threeSumClosest([0, 1, 2], 3))