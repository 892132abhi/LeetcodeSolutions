class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        res=[]
        res2=[]
        for i in range(1,n+1):
            if i%m==0:
                res.append(i)
            else:
                res2.append(i)
        return sum(res2)-sum(res)