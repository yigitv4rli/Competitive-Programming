class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr_index = 0
        last_nonzero_index = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums[i], nums[last_nonzero_index] = nums[last_nonzero_index], nums[i]
                last_nonzero_index +=1
