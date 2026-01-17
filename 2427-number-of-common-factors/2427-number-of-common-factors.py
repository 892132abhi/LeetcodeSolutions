class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        val = max(a,b)
        ans=[]
        for i in range(1,val+1):
            if a%i==0 and b%i==0:
                ans.append(i)
        return len(ans)