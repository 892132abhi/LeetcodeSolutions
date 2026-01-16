class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res =int(a,2)
        res2 = int(b,2)
        value = res+res2
        return format(value,"b")