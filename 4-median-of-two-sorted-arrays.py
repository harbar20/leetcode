class Solution:
    def __init__(self) -> None:
        pass
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        if len(merged) % 2 == 1:
            return merged[len(merged)//2]
        
        return (merged[len(merged)//2] + merged[len(merged)//2 - 1])/2
