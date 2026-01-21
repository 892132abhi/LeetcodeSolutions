class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = str(num)[::-1]
        res2 = int(str(int(res))[::-1])
        if num==res2:
            return True
        else:
            return False