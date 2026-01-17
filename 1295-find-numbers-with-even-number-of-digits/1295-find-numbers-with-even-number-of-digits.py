class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for i in nums:
            res = str(i)
            if len(res)%2==0:
                ans.append(i)
        return len(ans)