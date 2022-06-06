from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        length = len(nums)

        result = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            pivot = nums[i]
            j = i + 1
            k = length - 1
            while j < k:
                sum = nums[j] + nums[k]
                if sum == -pivot:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    continue
                if sum > -pivot:
                    k -= 1
                else:
                    j += 1

        return result

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))

# -4, -1, -1, 0, 1, 2