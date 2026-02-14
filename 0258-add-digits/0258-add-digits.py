class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = str(num)
        i = True
        while i :
            if len(a)>1:
                b=0
                for i in a:
                    b+=int(i)
                a = str(b)
            else:
                i = False
        return int(a)