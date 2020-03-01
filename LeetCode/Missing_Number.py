class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        current = 0
        
        if nums[0] != 0:
            return 0
        elif nums[-1] != len(nums):
            return nums[-1] +1
        
        for num in nums:
            if num == current:
                current +=1
            else:
                return current
            
