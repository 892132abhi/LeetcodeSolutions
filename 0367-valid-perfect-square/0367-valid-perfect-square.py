class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = round(pow(num,.5))
        if res*res==num:
            return True
        else:
            return False