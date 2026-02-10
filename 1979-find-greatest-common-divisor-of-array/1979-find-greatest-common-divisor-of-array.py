class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        a = max(nums)
        b = min(nums)
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                res.append(i)
        return max(res)