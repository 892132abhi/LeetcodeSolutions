class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        count=0
        for i in s:
            res = int(i)
            if num%res==0:
                count+=1
        return count