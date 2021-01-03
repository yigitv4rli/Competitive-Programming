class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set()
        
        for num in nums:
            seen.add(num)
        
        bestCount = 1
        for num in seen:
            if num-1 not in seen:
                count = 1
                currNum = num
                while currNum+1 in seen:
                    count+=1
                    currNum+=1
                bestCount = max(bestCount, count)
        return bestCount
                
