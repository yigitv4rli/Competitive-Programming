class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not len(nums):
            return [[]]
        partSol = self.subsets(nums[1:])
        return partSol + self.appendElement(nums[0], partSol)
    
    
    
    def appendElement(self, element, L):
        if not len(L):
            return []
        return [L[0] + [element]] + self.appendElement(element, L[1:])
        
