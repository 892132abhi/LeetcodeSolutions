class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)[::-1]
        print(num)
        if num!=str(x):
            return False
        else:
            return True