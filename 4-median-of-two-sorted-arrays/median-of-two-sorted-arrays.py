class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        merged = nums1+nums2
        merged.sort()
        length = len(merged)
        if length %2 ==0:
            median=(merged[length // 2 - 1] + merged[length // 2]) / 2.0
        else:
            median = merged[length//2]

        return median  