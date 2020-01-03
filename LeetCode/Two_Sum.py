class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for a in range(0,length):
            for b in range(a+1,length):
                if nums[a] + nums[b] == target:
                    return [a,b]
