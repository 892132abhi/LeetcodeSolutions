class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res =0
        res2=0
        for i in nums:
            if i <=9:
                res+=i
            else:
                res2+=i
        if res<res2 or res>res2:
            return True
        return False