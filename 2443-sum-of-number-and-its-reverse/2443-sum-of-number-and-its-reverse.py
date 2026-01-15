class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
                return True
        for i in range(1,num):
           
            res = int(str(i)[::-1])
            if res+i==num:
                return True
        return False