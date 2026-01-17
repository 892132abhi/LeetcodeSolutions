class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        res=1
        for i in range(1,n+1):
            res*=i
        res2 = str(res)[::-1]
        count=0
        for i in res2:
            if i!="0":
                break
            else:
                count+=1
        return count