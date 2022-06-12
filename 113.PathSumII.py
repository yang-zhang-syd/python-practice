class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []

        if not root.left and not root.right:
            if root.val == targetSum:
                return [[root.val]]
            else:
                return []

        leftLists = []
        if root.left:
            leftLists = self.pathSum_rec(root.left, root.val, targetSum, [root.val])
        
        rightLists = []
        if root.right:
            rightLists = self.pathSum_rec(root.right, root.val, targetSum, [root.val])

        return leftLists + rightLists
        
        
    def pathSum_rec(self, currentNode: Optional[TreeNode], prevSum: int, targetSum: int, path: List[int]) -> List[List[int]]:
        
        prevSum += currentNode.val

        if not currentNode.left and not currentNode.right:
            if prevSum == targetSum:
                path.append(currentNode.val)
                return [path]
            else:
                return []
        
        newPathLeft = list(path)
        newPathLeft.append(currentNode.val)

        leftLists = []
        if currentNode.left:
            leftLists = self.pathSum_rec(currentNode.left, prevSum, targetSum, newPathLeft)

        newPathRight = list(path)
        newPathRight.append(currentNode.val)

        rightLists = []
        if currentNode.right:
            rightLists = self.pathSum_rec(currentNode.right, prevSum, targetSum, newPathRight)

        return leftLists + rightLists
        