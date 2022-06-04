from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        productsLeft = [nums[0]]
        productsRight = [nums[length - 1]]

        for i in range(1, length):
            productsLeft.append(productsLeft[i - 1] * nums[i])

        for i in reversed(range(0, length - 1)):
            productsRight.insert(0, productsRight[0] * nums[i])

        results = []
        for i in range(length):
            left = productsLeft[i - 1] if i - 1 >= 0 else 1
            right = productsRight[i + 1] if i < length - 1 else 1
            results.append(left * right)
        
        return results

s = Solution()
r = s.productExceptSelf([1,2,3,4])
print(r)