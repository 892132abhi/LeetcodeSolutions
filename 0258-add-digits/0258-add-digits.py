class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res=num
        i = True
        while i:
            a = str(res)
            if len(a)>1:
                x = 0
                for i in a:
                    x+=int(i)
                res=x
            else:
                i = False
        return res