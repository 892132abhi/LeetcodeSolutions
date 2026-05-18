class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        num1 = str(int(num[::-1]))[::-1]
        return num1
        