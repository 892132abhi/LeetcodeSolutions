class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1 = [str(i) for i in nums]
        res=[]
        for i in num1:
            if len(i)>1:
                for j in i:
                    res.append(int(j))
            else:
                res.append(int(i))
        return res