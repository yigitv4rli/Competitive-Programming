class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num] +=1
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return [dic[i][0] for i in range(0,k)]
            
