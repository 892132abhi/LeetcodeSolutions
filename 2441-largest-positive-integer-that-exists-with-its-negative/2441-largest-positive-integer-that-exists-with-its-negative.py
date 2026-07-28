class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            if i>0:
                a=-i
                if i in nums and a in nums:
                    if res<i:
                        res=i
        if res>0:
            return res
        else:
            return -1
