from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        prefixSum = root.val
        prefixSumDic = {root.val: 1}
        
        count = 1 if prefixSum == targetSum else 0
            
        leftCount = self.pathSum_rec(root.left, targetSum, prefixSumDic, prefixSum)
        rightCount = self.pathSum_rec(root.right, targetSum, prefixSumDic, prefixSum) 

        return count + leftCount + rightCount

    def pathSum_rec(self, node: Optional[TreeNode], targetSum: int, prefixSumDic: dict, prefixSum: int) -> int:

        if not node:
            return 0

        newPrefixSum = prefixSum + node.val
        
        count = 1 if newPrefixSum == targetSum else 0

        diff = newPrefixSum - targetSum

        if diff in prefixSumDic:
            count += prefixSumDic[diff]
            
        copyDic = prefixSumDic.copy()

        if newPrefixSum in copyDic:
            copyDic[newPrefixSum] += 1
        else:
            copyDic[newPrefixSum] = 1

        leftCount = self.pathSum_rec(node.left, targetSum, copyDic, newPrefixSum)
        rightCount = self.pathSum_rec(node.right, targetSum, copyDic, newPrefixSum)

        return count + leftCount + rightCount