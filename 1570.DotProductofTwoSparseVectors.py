from typing import List

class SparseVector:

    def __init__(self, nums: List[int]):
        
        self.values = []

        for i in range(len(nums)):
            if nums[i] != 0:
                self.values.append((i, nums[i]))
            

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i = 0
        j = 0
        product = 0
        while i != len(self.values) and j != len(vec.values):
            index1 = self.values[i][0]
            index2 = vec.values[j][0]
            if index1 == index2:
                product += self.values[i][1] * vec.values[j][1]
                j += 1
                i += 1
            elif index1 > index2:
                j += 1
            else:
                i += 1
        return product



# Your SparseVector object will be instantiated and called as such:
v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
ans = v1.dotProduct(v2)
print(ans)