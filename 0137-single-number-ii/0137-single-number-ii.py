class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res={}
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        ans = min(res,key=res.get)
        return ans
        