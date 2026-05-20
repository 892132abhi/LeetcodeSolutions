class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        n1=nums[::-1]
        for i in nums:
            res.append(i)
        for i in n1:
            res.append(i)

        return res