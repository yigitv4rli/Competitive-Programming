class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        max_area = 0
        while p1 < p2:
            max_area = max((p2-p1) * min(height[p1],height[p2]), max_area)
            
            if height[p1] < height[p2]:
                p1 +=1
            else:
                p2 -=1
        return max_area
