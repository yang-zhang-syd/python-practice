class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''

        '''
        sumDic = {}

        currentSum = 0

        count = 0

        for num in nums:

            currentSum += num

            if currentSum == k:
                count += 1

            if currentSum - k in sumDic:
                count += sumDic[currentSum - k]

            if currentSum not in sumDic:
                sumDic[currentSum] = 1
            else:
                sumDic[currentSum] += 1

        return count