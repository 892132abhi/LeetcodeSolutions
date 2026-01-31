class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res= []
        a = min(nums)
        b = max(nums)
        for i in range(a,b):
            if i not in nums:
                res.append(i)
        return res