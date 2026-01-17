class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        val = list(str(n))
        val2 = [int(a) for a in val]
        pr = 1
        sm = 0
        for i in val2:
            sm +=i
            pr*=i
        res = pr+sm
        if n%res==0:
            return True
        else:
            return False