class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num] +=1
                
        for i in dic.keys():
            if dic[i] > len(nums) /2:
                return i
