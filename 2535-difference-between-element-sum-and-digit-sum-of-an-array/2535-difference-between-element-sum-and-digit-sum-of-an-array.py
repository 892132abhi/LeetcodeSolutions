class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        ans = sum(nums)
        for i in nums:
            a = str(i)
            if len(a)>1:
                for j in a:
                    res.append(int(j))
            else:
                res.append(int(a))
        return abs(ans-sum(res))