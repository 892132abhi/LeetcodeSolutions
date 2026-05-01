class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        res=0
        for a in accounts:
            n=0
            for b in a:
                n+=b
            if n>res:
                res = n
        return res
