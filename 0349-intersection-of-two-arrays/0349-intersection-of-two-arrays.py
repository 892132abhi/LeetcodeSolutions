class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res1 = set(nums1)
        res2 = set(nums2)
        res3 = res1.intersection(res2)
        res4 = list(res3)
        return res4