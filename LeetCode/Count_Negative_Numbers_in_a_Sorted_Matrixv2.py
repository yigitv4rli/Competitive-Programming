class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for matrix in grid:
            for number in matrix:
                if number < 0:
                    count +=1
                
        return count
                    
                
