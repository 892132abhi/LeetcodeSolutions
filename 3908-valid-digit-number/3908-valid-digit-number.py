class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        n1 = str(n)
        x1=str(x)
        if n1.count(x1)>=1 and n1[0]!=x1:
            return True
        return False