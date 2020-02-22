class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        dic = {}
                  
        def bitFinder(number):
            x = bin(number)[2:]
            bit_count = x.count("1")
            return bit_count
    
        for num in arr:
            bit_num = bitFinder(num)
            if bit_num in dic.keys():
                dic[bit_num] += [num]
            else:
                dic[bit_num] = [num]

        result = []
        for bits in sorted(dic.keys()):
            result += dic[bits]
        return result

