class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = nums1 + nums2
        merged_list = sorted(merged_list)
        length_merged = len(merged_list)
        
        if length_merged % 2 == 0:
            middle = length_merged / 2
            middle = int(middle)
            return (merged_list[middle-1] + merged_list[middle])/2      
        else:
            middle = length_merged // 2
            return merged_list[middle]
            
        
