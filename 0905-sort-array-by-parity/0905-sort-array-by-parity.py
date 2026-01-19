class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        ans=[]
        for i in nums:
            if i%2==0:
                res.append(i)
            else:
                ans.append(i)
        res.extend(ans)
        return res