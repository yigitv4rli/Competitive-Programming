class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeft(l,r, nums):
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] < target:
                    l = mid+1
                else:
                    r = mid -1
            return l
        
        def searchRight(l, r, nums):
            while l<=r:
                mid = (l+r) // 2
                
                if nums[mid] <= target:
                    l = mid+1
                else:
                    r = mid -1
            return r
        l, r = searchLeft(0, len(nums) -1, nums) ,searchRight(0, len(nums)-1, nums)
        return (l,r) if l <= r else [-1, -1]
            
