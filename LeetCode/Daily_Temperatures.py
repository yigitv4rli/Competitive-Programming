class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = list()
        for i in range(0,len(T)-1):
            day = 1
            for j in range(i+1,len(T)):
                if T[i] < T[j]:
                    result.append(day)
                    break
                else:
                    day +=1
            else:
                result.append(0)
        result.append(0)    
        return result
