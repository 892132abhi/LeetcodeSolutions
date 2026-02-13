class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        a = original
        i = True
        for i in nums:
            if a in nums:
                a*=2
            else:
                i = True
        return a