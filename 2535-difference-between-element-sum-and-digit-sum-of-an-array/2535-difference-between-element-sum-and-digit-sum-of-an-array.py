class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1 =[str(i) for i in nums]
        num2 = "".join(num1)
        num3 = list(num2)
        num4 = [int(i) for i in num3]
        sm = sum(nums)
        sm2 = sum(num4)
        return abs(sm-sm2)