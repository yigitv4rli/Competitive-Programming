class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(1,len(nums),2):
            a += nums[i-1] * [nums[i]]
        return a
