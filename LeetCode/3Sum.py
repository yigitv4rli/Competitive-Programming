class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        
        for i in range(0,len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            else:
                lower = i+1
                upper = len(nums) -1 
                while lower < upper:
                    if nums[lower] + nums[upper] + nums[i] == 0:
                        result.add((nums[lower], nums[upper], nums[i]))
                    
                    if 0-(nums[i]+nums[upper])>nums[lower]:
                        lower+=1
                    else:
                        upper-=1
                        
        return list(result)
