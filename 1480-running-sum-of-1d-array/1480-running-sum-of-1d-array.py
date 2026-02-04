class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        a=0
        for i in nums:
            a+=i
            res.append(a)
        return res
        